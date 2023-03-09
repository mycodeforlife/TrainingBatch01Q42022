class Calculater(object):

    def __init__ (self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def __add__ (self, num1, num2):
        answer = num1 + num2
        add = answer
        print('sum =', answer)

    def __sub__ (self, num1, num2):
        answer = num1 - num2
        print('difference =', answer)

    def __mul__ (self, num1, num2):
        answer = num1 * num2
        print('multiply =', answer)

    def __div__(self, num1, num2):
        answer = num1 / num2
        print('division =', answer)

    def __sign0__ (self, num1, num2):









