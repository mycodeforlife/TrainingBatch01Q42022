import sys

file_name = sys.argv[1]

fileobject = open(file_name,"r")
for eachline in fileobject:
    eachline = eachline.rstrip()
    print(eachline)
    fileobject.close()


