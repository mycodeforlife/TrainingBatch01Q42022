n = int(input(" please enter the n value:"))
for j in range(0,n+1):
    i = (n-j) *" " +j*" *"
    print(i)
for k in range(n-(n//2)):
    print((n-1)*" " +"*")
