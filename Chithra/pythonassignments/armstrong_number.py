
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
