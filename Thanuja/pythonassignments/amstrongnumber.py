i = int(input("enter the value:" ))
b = len(str(i))
temp = i
amstrong=0
while temp>0:
     a = temp%10
     amstrong  = amstrong+a **b
     temp//=10
     a =++temp
     print(amstrong)
     print(a)
     break
if amstrong==i:
    print("amstrong number")
else:
    print("not amstrong number")




