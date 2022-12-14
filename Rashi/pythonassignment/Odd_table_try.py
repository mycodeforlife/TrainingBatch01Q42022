def multi_table(a):
 for i in range (1,11):
     statement =str(a)+'*'+str(i)+'='+str(a*i)
     print (statement)

for k in range(1,20):
    if k%2!=0:
        multi_table(k)
        print("********************")


def num(a):
    if a%2==0:
        print(str(a)+" is even")
    else:
        print (str(a)+ " "
                       "is odd")

num(7)
