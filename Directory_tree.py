import os

# Aim to print Tree of directory structure

path=raw_input("Enter path to enemurate :")
for root,subfolders,files in os.walk(path):
    level=len(root.split("\\"))
    print  "-"*(level+4) + '[' + root.split('/')[-1] + ']'
    for file in files:
        print "-"*(level+12) + file
