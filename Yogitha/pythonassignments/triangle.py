print("Right Triangle")
trainglerows = int(input("Enter a number to print:  "))
for m in range(1, trainglerows+1):
    for n in range(1, m+1):
        print('*', end=' ')
    print()


print('Left Triangle')
for m in range(1, trainglerows+1):
    for i in range(m, trainglerows):
        print(end='  ')
    for n in range(1, m+1):
        print('*', end=' ')
    print()


print('Tree pattern')
for m in range(1, trainglerows+1):
    for i in range(m, trainglerows):
        print(end=' ')
    for n in range(1, m+1):
        print('*', end=' ')
    print()
print('    '+'*'+'   ')
print('    '+'*'+'   ')

print('reverse right angle Triangle')
for m in range(trainglerows+1,0,-1):
    for n in range(0, m-1):
        print('*', end=' ')
    print()


print('reverse left angle triangle')
for m in range(trainglerows,0,-1):
    for i in range(m-1, trainglerows):
        print(end='  ')
    for n in range(1, m+1):
        print('*', end=' ')
    print()









