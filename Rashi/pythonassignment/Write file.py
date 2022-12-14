#C:\Users\rahul\OneDrive\Documents\Zone_code_Python.txt
import sys
#input_file =input("enter the file name that you want to read:")
input_file= sys.argv[1]
zip_code_map= {}

File1= open(input_file,"r")
for eachline in File1:
    eachline = eachline.rstrip()
    data=eachline.split(",")
    #print (data[0], data[1])
    zip_code_map[data[0]]=data[1]
    #for each in data:
        #print(each)
File1.close()
output_file = sys.argv[2]
outfile= open(output_file,"w")

for eachzip in zip_code_map.keys():
    #print(eachzip, zip_code_map[eachzip])
    #line= eachzip+" "+zip_code_map[eachzip]+"\n"
    line = "Insert into Zone_table (Zipcode,Zone_id) values ("+eachzip + ",'" + zip_code_map[eachzip] + "')"+";\n"
    outfile.write(line)

outfile.close()
