
n=int(input("Please enter the n value:"))
for i in range(0,n):
    j = (n-i-1)*" " + i*"*"
    print(j, end=" ")
    print()

n=int(input("Please enter the n value:"))
for i in range(n-1,0,-1):
    j = (n-i)*" " + i*"*"
    print(j, end=" ")
    print()


n=int(input("Please enter the n value:"))
for i in range(0,n):
    j = i*"*"
    print(j, end=" ")
    print()

n=int(input("Please enter the n value:"))
for i in range(n-1,0,-1):
    j = i*"*"
    print(j, end=" ")
    print()

n=int(input("Please enter the n value:"))
for i in range(0,n):
    for j in range(n-i-1,0,-1):
        print(" ",end="")
    for j in range(0,i):
        print("*", end=" ")
    print()
for k in range (n+1,n+3):
    print("  " + "*")
print()
