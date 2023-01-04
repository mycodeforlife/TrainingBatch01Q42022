cal = input("enter what arthamatic operation you want to do add,sub,mul and div")
value_type =input( "enter what type of athamatic operation you want int or float : ")


def add2number(value1, value2):
    a = value1 + value2
    return a


def numberdiff(value1, value2):
    return value1 - value2


def multiplication(value3, value4):
    return value3 * value4


def div_two(value1, value2):
    return value1 // value2


x = input("enter the value for addition: ")
y = input("enter the value for subtraction: ")

if value_type == int:
    x = int(x)
    y = int(y)
else:
    value_type == float
    x = float(x)
    y = float(y)

if cal == "add":
    total = add2number(x, y)
    print(total)
elif cal == "sub":
    print(numberdiff(x, y))
elif cal == "mul":
    multiplytwo = multiplication(x, y)
    print(multiplytwo)
else:
    var = cal == 'div'
    divition_of_two = div_two(x, y)
    print(divition_of_two)
