#multiplication table#

n=int(input("Please enter the n value:"))
for i in range(1,n+1):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print()

#fibonacci series#

n=int(input("Please enter the n value:"))
x = 0
y = 1

for i in range(0,n):
    if (i<=1):
        print(i)
    else:
        i = x + y
        x = y
        y = i
        print(i)
    print()

#armstrong Number#
n=input("Please enter the n value:")
x =len(n)
a = 0
for i in range(0,x):
    y = int(n[i])
    z = y**x
    a = a + z
print(a)
if (a == int(n)):
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")


#prime numbers

    
