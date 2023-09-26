def mul(a):
    for i in range(1, 11):
        multi = str(a) + "*" + str(i) + "=" + str(a * i)
        print(multi)


'''
following function will check list of even numbers from 1 to 9 
and then if its even number calling multiplicaiton table using mul function call
'''

"""
def even():
    for a in range(1, 10):
        if a % 2 == 0:
            mul(a)
"""


def odd():
    for b in range(1, 11):
        if b % 2 != 0:
            mul(b)


odd()

