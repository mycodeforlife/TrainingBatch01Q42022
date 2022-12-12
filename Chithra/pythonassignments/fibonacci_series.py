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
