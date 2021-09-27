################################################################################
# Tuanaliza ruchu przez porty z listy                                          #
################################################################################
import pyshark 
import os
import time
#tytajtworzenie własnych narzędzi może być dosć trudne, więc korzystać będę z biblioteki pyshark
#umożliwia ona parsowanie danych z wiresharka/tsharka
#prawdopobonie większość rzeczy mogłbym zrobić za pomocą wiresharka
#plan jest taki, że dla wyszukanych wcześniej portów, wykonam analiżeruchu wiresharkiem/tsharkiem
#następnie parsując za pomocą pysharka wybiore odpowiednie informacje
'''
capture = pyshark.LiveCapture(interface='eth0')
capture.set_debug()
capture.sniff(timeout=50)
capture[3]
'''
scan_nr = 0
port_nr = 80


 
class Portanalyzer:
    def __init__(self, name):
        self.name = name
        self.port_number = 0
        self.scan_number = 0
        self.duration = 0
        self.capture_tab = []
    
    #########przechwytywanie ruchu do okreslonego folderu  
    
    def capture(self):
    
        command = os.system('tshark -f "port {0}" -i any -w "traffic/{3}_scan_{1}/tmp_out_{0}" -a duration:{2}'.format(self.port_number,self.scan_number, self.duration, self.name))
        print("executed with code %s" % command)
        
    ##########parsowanie pysharkiem
        
    def parse(self, cap_nr):
        self.cap = pyshark.FileCapture('traffic/{2}_scan_{1}/tmp_out_{0}'.format(self.port_number, self.scan_number, self.name))
        '''
        try:
            return cap[cap_nr]
        except KeyError:
            print("empty")
            return KeyError
        '''   
    ##########wywołanie   
            
    def scan(self):
        self.scan_number = self.scan_number + 1
        print("Scan number: ", self.scan_number)
        
        os.system("mkdir traffic/{1}_scan_{0}".format(self.scan_number, self.name))

        self.capture()
        '''
        code = 0
        while(self.parse(code) != KeyError):
            print("Cap nr: ", code)
            time.sleep(3)
            print(self.parse(code))
            code = code +1
        '''
        self.parse(0)
            
    def set_env(self, port, duration):
        self.port_number = port
        self.duration = duration
        
    
    def printer(self):
        print(self.name, self.port_number, self.scan_number,\
            self.duration, self.capture_tab )
      
    
    def return_cap(self, nr):
        return self.cap[nr]
        
        
'''
test = Portanalyzer(80)
test.set_env(80, 10)
test.printer()        
test.scan()

test2 = Portanalyzer(23)
test2.set_env(23, 3)
test2.printer()        
test2.scan()


test2 = Portanalyzer(69)
test2.set_env(69, 3)
test2.printer()        
test2.scan()
'''  