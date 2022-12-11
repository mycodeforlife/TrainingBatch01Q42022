n=int(input("Please enter the n value:"))
for i in range(1,n):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(1,n):
    for j in range(1, i + 1):
        print("*", end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(1,n):
    for j in range(i):
        print(i, end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    for j in range(i):
        print(i, end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(0,n):
    for j in range(i+1,0,-1):
        print(j, end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    for j in range(i-1,0,-1):
        print(j, end="")
    print()

n=1
c=1
for i in range(1,5):
    for j in range(1,c+1):
        print(n, end="")
        n=n+1
    c=c+2
    print()

n=int(input("Please enter the n value:"))
for i in range(1,n+1):
    j = (n-i)*" "+i*"*"
    print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(1,n):
    j = i*"*"
    print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    j = i*"*"
    print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(n,0,-1):
    j = (n-i)*" "+ i*"*"
    print(j,end="")
    print()

n=int(input("Please enter the n value:"))
for i in range(1,n):
    for j in range(1,n-i):
       print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    print()

