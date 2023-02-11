import Person
import Student
import Parent


class Teacher(Person, Student, Parent):
    Teacher_obj = Person()
    Student_obj = Student()
    Parent_obj = Parent()
    Marks = 0
    Class_Subject = {}  # { "Grade6": ["math","Science"],"Grade8": ["math"],"Grade5": ["math","Social"]

    def __init__(self):
        self.Teacher_obj = Person()
        self.Student_obj = Student()
        self.Parent_obj = Parent()

    def set_teacher_name(self, last_name, first_name):
        self.person.set_person_name(last_name, first_name)

    def set_teacher_income(self, amount):
        self.parent_obj.set_teacher_income(amount)

    def set_job_tittle(self, job_tittle):
        self.parent_obj.set_job_tittle(job_tittle)

    def set_child_details(self, last_name, first_name):
        self.child_obj.set_child_details(last_name, first_name)

    def assign_class_subject(self, grade_info, subject_list):
        grade_key = "Grade" + str(grade_info)
        self.class_subject[grade_key] = subject_list

    def associate_grade_student_info(self, grade_info, student_name_list):
        pass

    def set_child_marks(self, Subject_Marks):
        self.Marks = Subject_Marks

    def set_teacher_contact_details(self, email_id, phonenum, address, zip_code):
        self.person.set_person_contact_details(email_id, phonenum, address, zip_code)

    def get_teacher_name(self):
        return self.set_teacher_name

