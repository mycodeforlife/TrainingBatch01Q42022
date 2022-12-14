"""
Following lines of code will print multiplication table from 1 to 14 numbers
"""
# for i in range (1,15) - is for generating number from 1 to 14
for i in range (1,15):
    # next for loop is to generate 1 to 10 number so that we can multiply initial i value with 1 to 10 number
    # one after other
    for j in range(1,11):
        print (i,"x",j,"=",i*j,end='\t')
    print ()