from subprocess import Popen, PIPE
import os

print ("Type in your IP address in this format: \"aa.aa.aa.aa\"\n")

IP = input ("Enter your IP address: ")

command = "curl ip-api.com/" +IP

try:
    CMD = Popen(command, shell = True, stdout = PIPE, stderr = PIPE)
    print (CMD.stdout.read().decode('utf-8'))
except:
    print ("An error occured\n")
    print (CMD.stderr.read().decode('utf-8'))
