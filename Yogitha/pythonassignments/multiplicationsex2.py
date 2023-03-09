def multi_table(a):
    for j in range(1, 11):
        statement = str(a) + 'x' + str(j) + '=' + str(a * j)
        print(statement)


multi_table(8)


def even_number():
    for i in range(1, 21):
        if i % 2 == 0:
            multi_table(i)
        # print("---")
even_number()


def odd_number():
    for a in range(1, 11):
        if a % 2 == 1:
            multi_table(a)
odd_number()








