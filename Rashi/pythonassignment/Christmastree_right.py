n = int(input(" please enter the n value:"))
for j in range(n,0,-1):
    i = (j-1) *" " + (n-j+1)*"*"
    print(i)

