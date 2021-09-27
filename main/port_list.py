################################################################################
# Tu pozyskiwanie listy otwartych portów(skaner)                               #
# być może zostanie zaimplementowana wielowątkowość,                           #
# gdyż niska ilość skanów, daje małą dokładność                                #
################################################################################

import subprocess, socket, sys, os

class Portlister:
    def __init__(self): #prosty konstruktor bezparametrowy
        self.portlist = []
        self.timeout = 0.000001 #czas oczekiwania na odpowiedź - lokalne porty, więc minimalny
        self.ip = 0
        self.host = ""

################################################################################
#ręczne ustawianie hostów
    def set_host(self, host):
        self.host = host

    def set_timeout(self, time):#ustawiamy czas oczekiwania  na odpowuiedź
        self.timeout = time
    
################################################################################
#automatyczne ustawianie hosta 
    def localhost(self):
        self.host = socket.gethostbyname("localhost") #dla testów używam localhost

    def localip(self):
        '''
        hostname = socket.gethostname()
        self.host = socket.gethostbyname(hostname)
        '''
        result = subprocess.check_output("hostname -I | awk '{print $1}'", shell=True)
        self.host = str(result)[2:-3]

################################################################################
# ta funkcja podaje ip ustawionego na obiekcie hosta
    def getip(self):
        if self.host == None:
            print("Host not set\n")
        else:
            return socket.gethostbyname(self.host)

################################################################################

    def scanports(self, start, end):
        temp_list = [] #tymczasowa lista
   
        for port in range(start, end+1):  #skan w zakresie
            #tworzę socket ipv4, 
            temp_socket = socket.socket(2, 1) #socket.AF_INET, socket.SOCK_STREAM 
           
            temp_socket.settimeout(self.timeout) #czas oczekiwania na odpowiedź - lokalne porty, więc minimalny
            #location = ("192.168.1.1", port)
            #tutaj mały problem z czasem trwania, zwrot podobny do zastosowania nmap, 
            # potrójny skan zajął 253 sekundy, czyli szybciej niż nmapem, jednak mniej dokładnie
            #rozpatruję rozwiącanie wielowątkowością, bądź zwiększonym czasem na odpowiedź
            #ale nawet pół sekundy przy tylu portach będzie kłopotliwe
            #narazie zostawiam, jako szkielet skanera portów, dptymalizacja przyjdzie później
            location = (self.host, port)
            result = temp_socket.connect_ex(location)  #
        #próba utworzenia połączenia z portem, zwraca kody błędu połączenia, 0 gdy brak
            if result == 0:
                print("Port opened on %d" % port)
                temp_list.append(port)
            temp_socket.close()   #zamykam socket 
            
        return temp_list
    
################################################################################

    def perform_scan(self, times, start, end):
        for x in range(times): #wykonuję skan 'times' razy 
            self.portlist += (self.scanports(start, end))# i dorzucam do listy
        
################################################################################

    def get_ports(self):
        self.portlist = list(set(self.portlist)) #usuwam powtórzenia
        return self.portlist # zwracam gotową listę
    
    def __str__(self):
        return self.host
    
################################################################################
"""
x = Portlister()
#x.localip()
x.localhost()
print(x.getip())

x.perform_scan(3, 0, 65535)
lista = x.get_ports()
print(lista)
"""
'''
xen = Portlister()
xen.localip()
print(xen)
'''