#plik do testów


import socket  #importing library  

def dumper():
    print(socket.gethostbyname("localhost"))
        
        
def host_open_ports(): 
    port_list = []
    ip = socket.gethostbyname ("localhost")  #getting ip-address of host 
    
    for port in range(0, 65535+1):
        test_socket = socket.socket(2, 1) #socket.AF_INET, socket.SOCK_STREAM
        location = (ip, port)
        result = test_socket.connect_ex(location) 
        #próba utworzenia połączenia z portem, zwraca kody błędu połączenia, 0 gdy brak
        if result == 0:
            print("Port opened on %d" % port)
            port_list.append(port)
        test_socket.close()
    print(port_list)
    
    
import subprocess
'''
proc = subprocess.Popen(["lsof -i"], stdout=subprocess.PIPE, shell=True)
out, err = proc.communicate()
print ("network connections output:")
print (out)
'''
scan_nr = 0
port_nr = 80
import os
def capture(port_number, scan_number):
    
    command = os.system('tshark -f "port {0}" -i any -w "traffic/tmp_out_{0}" -a duration:10'.format(port_number,scan_number))
    print("executed with code %s" % command)

import pyshark
def parse(port_number, scan_number):
    cap = pyshark.FileCapture('traffic/tmp_out_{0}'.format(port_number, scan_number))
    try:
        print(cap[0])
    except KeyError:
        print("empty")

def sccn():
    global scan_nr, port_nr
    try:
        os.system("mkdir traffic/scan%i" %scan_nr)
    except FileExistsError:
        pass
    scan_nr = scan_nr + 1
    capture(port_nr, scan_nr)
    parse(port_nr, scan_nr)
    
sccn()
   
'''
# A simple Python program to demonstrate 
# getpass.getpass() to read password
import getpass
  
try:
    p = getpass.getpass()
except Exception as error:
    print('ERROR', error)
else:
    print('Password entered:', p)
 '''   
    
    
#sccn() <-dziala
'''
os.popen("sudo -S %s"%(command), 'w').write(password)
'''
#https://creodias.eu/-/how-to-open-ports-in-linux-

#'ufw enable'
#sudo ufw allow (port)/tcp <- ufw będzie odpowiednie 
#plan: po uzyskaniu "otwartych" portów nastąpi interakcja z użytkownikiem
#wersja robocza
#Uwaga! Istnieje ryzyko kompromitacji systemu!
#Zalecane działania:
#Program **** zablokuje ruch przez podejrzane porty
#Nastepnie zalecane będzie dokładne skanowanie systemu za pomocą aktualnego AntyWirusa
#Po zakończeniu niezbędnych czynności program, przywróci porty do pierwotnego stanu
