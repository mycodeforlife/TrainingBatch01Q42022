class Student:

    first_name = "none"
    last_name = "0"
    email_address = "none"
    postal_address = "0"

    def __init__(self, first_name, last_name):
        self.student_first_name = first_name
        self.student_last_name = last_name

    def personal_details(self, email_address, postal_address):
        self.email_address = email_address
        self.postal_address = postal_address

    student_id = ""
    year = ""
    class_info = ""

    def student_marks(self, student_id, year, class_info):
        self.student_id = student_id
        self.year = year
        self.class_info = class_info

    def get_student(self):
        return self.student_first_name, self.student_last_name

    def get_student_marks(self):
        return self.student_id, self.year, self.class_info

    def get_personal_details(self):
        return self.email_address, self.postal_address


student1 = Student("Aarna", "Dama")
student1.student_marks("1002", "2020", "sectionA")
student1.personal_details("ad@gmail.com","Va Beach, 23464")
print(student1.get_student())
print(student1.get_personal_details())
print(student1.get_student_marks())
print()
student2 = Student("sriram", "kora")
student2.student_marks("1003", "2021", "sectionB")
student2.personal_details("sk@gmail.com", "Va beach, 23464")
print(student2.get_student())
print(student2.get_personal_details())
print(student2.get_student_marks())







