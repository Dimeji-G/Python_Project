#ifconfig "interface down"
#ifconfig "interface" hw ether "new Mac"
#ifconfig "interface" up
import subprocess
import re
from subprocess import Popen, PIPE

iface = input("Enter your interface name: ")
new_mac = input("Enter your desired Mac address in this: ")

class Mac:
    def __init__(self):
        self.MAC = ""

    def get_MAC(self, interface):
        CMD = subprocess.run("ifconfig " + interface, shell = True,capture_output = True)
        result = CMD.stdout.decode('utf-8')
        #print (result)

        pattern = r'ether\s[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}:[\da-z]{2}'
        precise = re.compile(pattern)
        ans = precise.search(result)
        answ = ans.group().split(" ")[1]
        print ("\nYour Old Mac Address is:", answ)

    def new_MAC(self,interface):
        command = "ifconfig " + interface + " hw ether "+ new_mac
        # print (command)
        up = "ifconfig " + iface + " up"
        down = "ifconfig " + iface + " down"
        subprocess.run(down, shell = True)
        cmde = Popen(command, shell = True, stdout = PIPE)
        subprocess.run(up, shell = True)
        print ("\nYour Mac address has been changed to: " + new_mac )


Mac.get_MAC('self', iface)
Mac.new_MAC('self', iface)
