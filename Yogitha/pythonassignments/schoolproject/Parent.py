import Person
import Student


class Parent(Person.Person):

    person = "none"
    annual_income = "0"
    employee_details = "none"

    def __init__(self):
        self.person = Person()
        self.child_obj = Student()

    def set_parent_name(self, firstname, lastname):
        self.person.set_person_name(firstname, lastname)

    def set_annual_income(self, income):
        self.annual_income = income

    def set_employee_details(self, teacher):
        self.employee_details = teacher

    def set_child_details(self, first_name, last_name):
        self.child_obj.set

    def get_parent(self):
        return self.parent_first_nmae, self.parent_last_name

    def get_annual_income(self):
        return self.amount

    def get_employee_details(self):
        return self.teacher

    def get_child_details(self):
        return self.Student
