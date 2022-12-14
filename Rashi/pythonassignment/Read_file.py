#C:\Users\rahul\OneDrive\Documents\File_for Python.txt

input_file =input("enter the file name that you want to read:")
File1= open(input_file,"r")

for eachline in File1:
    eachline = eachline.rstrip()
    print(eachline)
File1.close()