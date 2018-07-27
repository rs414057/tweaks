from _winreg import *
import os

def identify_os():
    if(os.name=="nt"):
        """print r"*** Reading usb logs history ***" """
        aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)

        aKey = OpenKey(aReg, r"SYSTEM\CurrentControlSet\Enum\USBSTOR")
        for i in range(1024):
            try:
                asubkey_name = EnumKey(aKey, i)
                print asubkey_name
               
            except EnvironmentError:
                break
    elif(os.name=="linux"):
        with open("/var/log/message") as fh:
            for line in fh:
                if("usb" in line):
                    print "line of usb",line




identify_os()

