import sys

#input_file =input("enter the file name that you want to read:")
input_file = sys.argv[1]
#print(input_file)
zip_code_map= {}
File1=open(input_file,"r")
for each in File1:
    each= each.rstrip()
    data= each.split(",")
    #print("line = "+each)
   # print("data = "+data[0], data[1],data[2])

    zip_code_map[data[0]]=data[1]
File1.close()

output_file= sys.argv[2]
out= open(output_file,"w")

for eachline in zip_code_map.keys():
    line="insert int zone_table values (zip_code, zone_id) values ("+eachline+" "+"'"+zip_code_map[eachline]+ "')"+"\n"
    out.write(line)
out.close()