n = int(input("Enter a number: "))
i = 0
result = n
while result > 0:
   m = result % 10
   i += m ** 3
   result //= 10
if n == i:
   print(n," It is an Armstrong number")
else:
   print(n," It is not an Armstrong number")






