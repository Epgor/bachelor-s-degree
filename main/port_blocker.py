################################################################################
# Tu tworzenie reguł blokowania niechcianego ruchu/ konfiguracja firewall      #
################################################################################
import os, subprocess

class PortBlocker:
    def __init__(self, name):
        self.name = name
        self.portlist = []
        self.password = ""

        
    def SetPorts(self, ports):
        self.portlist = ports
    
    def ActivateBlocker(self):
        try:
            #tutaj pytamy graficznie o hasło
            os.popen("sudo -S %s"%('ufw enable'), 'w').write(self.password)
            return 0
        except:
            return 1
        
    def BlockPorts(self):
        for port in self.portlist:
            command = "ufw deny %i"% port
            os.popen("sudo -S %s"%(command), 'w').write(self.password)
            #os.system(command)
    
    def DeactivateBlocker(self):
        try:
            #tutaj pytamy graficznie o hasło
            os.popen("sudo -S %s"%('ufw disable'), 'w').write(self.password)
            return 0
        except:
            return 3
    
    def SavePorts(self):
        with open(('block/{0}/{0}_blocker.txt').format(self.name), "w") as f:
            for port in self.portlist:
                f.write(str(port)+"\n")
                
            
    def LoadPorts(self):
        with open(('block/{0}/{0}_blocker.txt').format(self.name), "r") as f:
            for port in f.readlines():
                self.portlist.append(int(port))
                
    def ResetFirewall(self):
        os.popen("sudo -S %s"%('ufw --force reset'), 'w').write(self.password)
        #os.system("xdotool key y")
                
    def ReturnPorts(self):
        return self.portlist
    
    def WhatsMyName(self):
        return self.name
    
    def Clear(self):
        os.system("xdotool key Escape")
        
    def SetPasswd(self, password):
        self.password = password
        
    
    
'''
B = PortBlocker('testowy')
print(B.WhatsMyName())
B.SetPorts([20,30,40])
B.SavePorts()
B.ClearPorts()
B.LoadPorts()
print(B.ReturnPorts())


B1 = PortBlocker('test2')
print(B1.WhatsMyName())
B1.SetPorts([23,33,43])
B1.SavePorts()
B1.ClearPorts()
B1.SetPorts(B.ReturnPorts())
print(B1.ReturnPorts()) <- klasa umożliwia przepisywanie portów między obiektami


A = PortBlocker('du')
A.ActivateBlocker()
#A.DeactivateBlocker()
A.Clear()
print(A.WhatsMyName())
A.SetPorts([65001, 65002])
A.BlockPorts()
input()
A.DeactivateBlocker()

'''