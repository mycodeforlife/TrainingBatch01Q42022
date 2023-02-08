#defining function and calling that function

def function():
    print("Welcome")
    print("Thank you")
function()

print("-----------------")

#multiplying different numbers and returning those values to seperate variables

def multiple_value(number):
    return(number*5)
a = multiple_value(2)
print(a)

print("-----------------")

b=multiple_value(5)
print(b)

print("-----------------")

c=multiple_value(10)
print(c)

print("-----------------")

#adding 2 numbers and return the value in a variable

def addition(number1,number2):
    return(number1+number2)
e = addition(40,30)
print(e)

print("-----------------")


#Not returning the value to function

def function1(x):
    print(x)
    print("still in this function")
    return(3*x)
f = function1(4)

print("-----------------")



#Returning the value to function

def function2(x):
    print(x)
    print("still in this function")
    return(3*x)
g = function2(4)
print(f)

print("-----------------")

#converting miles to kilometer

def convert_miles_km(miles):
    return(miles*1.609)
h = int(convert_miles_km(4))
print(h)

print("-----------------")

