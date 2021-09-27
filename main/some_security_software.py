###########################################################
###########################################################
###########################################################
#       Program do wykrywania luk w zabezpieczeniach      # 
#                 systemu operacyjnego                    #
###########################################################
#               Autor : Bartosz Wiśniewski                #
###########################################################
###########################################################
###########################################################
###########################################################

#from dump import *
from port_list import *
from port_info import *
from port_anal import *
from port_blocker import *

import sys, os


class ZubrSecurity(Portlister, Portinformer, Portanalyzer, PortBlocker):
    def __init__(self, name):
        super().__init__()   
        self.name = name
        self.portlist = []
        self.results = []
        self.port_informer_string = ""
        self.port_informer_string_list = []
        self.port_number = 0
        self.scan_number = 0
        self.duration = 0
        self.capture_tab = []
        self.password = ""
        os.system("mkdir block/{}".format(self.name))

    def listen(self, scans, ports):
        p_beg = 0
        p_end = 0
        if ports == 1:
            p_beg = 0
            p_end = 1024
        elif ports == 2:
            p_beg = 1024
            p_beg = 65535
        else:
            p_beg = 0
            p_end = 65535 
        
        self.perform_scan(scans, p_beg, p_end)
        
                        
    def ClearPorts(self):
        self.portlist.clear()

    def __str__(self):
        return "Hi. I'm an instance of Zubr Security Software. \n" \
            + "My name is %s" % self.name

        



def main():
    
    #x = Portlister() #tworzę obiekt do nasłuchiwania portwó
    #x.set_host("localhost") #localhost dla testów, program będzie sprawdzał połączenia przez wszystkie dostępne sieci
    #x.perform_scan(1, 0, 65535) #szybki skan dla wszystkich portów (ilość skanów, zakres portów od, do)
    #lista = x.get_ports()
    
    lista = [80, 11, 26910] #do testów
    print(lista)
    '''
    y = Portinformer() #tworzę obiekt do generowania informaci o liscie portów
    y.read("data/portinfo.csv")
    y.search(lista)
    '''
    
    
    '''
    p_a = Portanalyzer("test")
    p_a.set_env(port = 80, duration = 20)
    ###konstrukcja do testów, bo nie zawsze skan natrafi na ruch
    #p_a.scan()
    p_a.scan_number = 2
    #p_a.scan()
    p_a.parse(0)
    
    error = 0
    cap = 0
    while(error == 0):
        print("Cap number: ",cap)
        try:
            print(p_a.return_cap(cap))
            cap = cap +1
        except KeyError:
            error = 1
            print("Empty")
    '''
    block = PortBlocker('block')
    print(block.WhatsMyName())
    block.SetPorts(lista)
    block.SavePorts()
    block.ClearPorts()
    block.LoadPorts()
    print(block.ReturnPorts())

    
    block.ActivateBlocker()
    
    block.BlockPorts()
    
    block.DeactivateBlocker()
    
    block.ResetFirewall()

if __name__ == "__main__":
    ###############obiektowość jest fajna :D
    #main()
    ######buduję szklelet funkcji które będą inicjowane przez gui
    '''
    zuberek = ZubrSecurity("ninja")
    ##############portanalyzer########
    print(zuberek)
    zuberek.set_timeout(0.00001)
    zuberek.localhost()
    print(zuberek.getip())
    print(zuberek.WhatsMyName())
    zuberek.listen(1,1)
    print(zuberek.get_ports())
    
    
    zuberek.set_host("test")
    print(zuberek.return_ip())
    zuberek.timeout(0.00001)
    zuberek.listen(1, 1)
    print(zuberek.return_ports)
    
        
    lista = [3422, 80, 11, 26910, 80, 29100] #do testów
    print(lista)
    
    y = Portinformer() #tworzę obiekt do generowania informaci o liscie portów
    y.read("data/portinfo.csv")
    y.search(lista)
    llista = y.return_list()
    for _ in range(len(llista)):
        print(llista[_])

    '''
    #uberek = ZubrSecurity("ninja")
   # print(uberek.null_print(10))
#    uberek.read("data/portinfo.csv")
   # uberek.results
    #print(uberek.WhatsMyName())
    #uberek.results