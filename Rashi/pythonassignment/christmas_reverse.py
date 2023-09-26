n = int(input(" please enter the n value:"))
for i in range(n,0,-1):
    j = (n-1) *" " + i*"*"
    print(j,end="")
    print()