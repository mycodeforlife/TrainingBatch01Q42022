num=0
b=1
max=10

for x in range(0,max):
    if x<=1:#0 1 2 3 4
        result=x
        print(result)
     #print(x)
    else:
        result=num+b#r=0+1=1 1+1=2 1+2=3
        num=b#n=1 n=1 n=2
        b=result#b=1 b=2 b=3
        print(result)

