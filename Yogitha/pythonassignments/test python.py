"""
Read the student marks from the file and print student id who got marks below 30
"""
import sys

file_name = sys.argv[1]
student_list = {}
try:
    file1 = open(file_name, "r")
except:
    print(file_name, "does not exists")
else:
    for each_line in file1:
        each_line = each_line.rstrip()
        student_marks = each_line.split("-")
        print(student_marks)
        student_list[student_marks[0]] = student_marks[1]
        print(student_list)
    file1.close()
