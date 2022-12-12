n = int(input(" please enter the n value:"))
j=0
for i in range(2, n):
    if n % i == 0:
        j= 1
        break
if j==0:
    print(n, ' is a prime number')
else:
    print(n, " is a composite number")
