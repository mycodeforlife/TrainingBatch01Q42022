import sys

file_name = sys.argv[0]
file_operation = sys.argv[1]
file_content = sys.argv[2]

fileobject = open(file_name, file_operation)
if file_operation == "r":
    for eachline in fileobject:
        eachline = eachline.rstrip()
        print(eachline)
elif file_operation == "w":
    fileobject.write(file_content)
else:
    print("please enter valid file operation, it must be r/w")

fileobject.close()
