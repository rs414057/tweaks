import platform
if (platform.system()=="Linux"):
    #usb logs history stored in /var/log/messages
    with open("/var/log/messages") as f:
        for lines in f:
            if "usb" in lines:
                print lines

