import Person
import Teacher


class Student(Person.Person):

    first_name = "none"
    last_name = "0"
    email_address = "none"
    postal_address = "0"
    zip_code = "0"
    Date_of_birth = "0"
    gender = ""

    def __init__(self):
        self.person_student = Person()
        self.Teacher_obj = Teacher()

    def student_details(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def set_student_gender(self, gender):
        self.person_student.set_student_gender(gender)

    def student_contact_details(self, email_address, phone_number, postal_address, zip_code):
        self.email_address = email_address
        self.phone_number = phone_number
        self.postal_address = postal_address
        self.zip_code = zip_code

    def acess_marks(self, Eng, Math, Science, Social):
        self.Teacher_obj.acess_Marks(Eng, Math, Science, Social)

        specific_grade_mark_info_dict_list = []
        for each_grade in perfdict.keys():
            specific_grade_mark_info_dict_list = perfdict[each_grade]
            specific_grade_mark_info_dict_list.append(specific_grade_mark_info_dict_list)
        return specific_grade_mark_info_dict_list

    def get_student(self):
        return self.first_name, self.last_name

    def get_student_gender(self):
        return self.gender

    def get_student_contact_details(self):
        return self.email_address, self.postal_address, self.zip_code




