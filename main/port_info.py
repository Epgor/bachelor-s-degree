################################################################################
# Tu info o portach - ładowane z pliku data/portinfo.txt                       #
################################################################################
import csv
import os
class Portinformer:
    def __init__(self): #prosty konstruktor bezparametrowy
        self.portlist = []
        self.results = []
        self.port_informer_string = ""
        self.port_informer_string_list = []


    def return_list(self):
        return self.port_informer_string_list

    def info_printer(self, x, port):
        self.port_informer_string = ""
        self.port_informer_string += ("Info about port - " + str(port)+ " : \n")
        self.port_informer_string += ("TCP: ")
        self.port_informer_string += ('\n' + ''.join(self.results[x][1]) +'\n')
        self.port_informer_string += ("UDP: ")
        self.port_informer_string += ('\n' + ''.join(self.results[x][2])+'\n')
        self.port_informer_string += ("Description: ")
        self.port_informer_string += ('\n' + ''.join(self.results[x][3])+'\n')
        self.port_informer_string += ("IANA status: ")
        self.port_informer_string += ('\n' + ''.join(self.results[x][4])+'\n')
        return self.port_informer_string

    def null_print(self, port):
        self.port_informer_string = ""
        self.port_informer_string += ("Info about port - "+ str(port)+ " : \n")
        self.port_informer_string += ("Info not available. Check the Internet \n")
        return self.port_informer_string
    
    def read(self, f_path):
        self.results.clear()
        dir = os.path.dirname(__file__) #<-- absolute dir the script is in
        rel_path = f_path
        file_path = os.path.join(dir, rel_path)

        with open(file_path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader: # each row is a list
                self.results.append(row)
    
    def search(self, l_ports):        
        #print(type(results[23][0]))
        self.port_informer_string_list.clear()
        self.portlist = l_ports      

        for port in self.portlist:
            search_flag = 0
            for x in range(len(self.results)):
                    if(str(port) == self.results[x][0]):
                        self.port_informer_string_list.append(self.info_printer(x, port)) #dostępne info o porcie
                        search_flag = 1

                
            if (search_flag) == 0: #do optymalizaji - wyszukiwanie w zakresach podanych w pliku .csv
                for z in range(len(self.results)):
                    if '-' in self.results[z][0]:
                        s = self.results[z][0]
                        xr = map(str.strip,s.split('-'))
                        lista = list(map(int,xr))
                        if int(port) in range(lista[0], lista[1]+1):
                            self.port_informer_string_list.append(self.info_printer(z, port))
                            search_flag = 1
                            
            if (search_flag) == 0:
                self.port_informer_string_list.append(self.null_print(port))
                
