"""
Read the student marks from the file and print student id who marks are below 40
"""
import sys

file_name = sys.argv[1]
student_list = {}
file1 = open(file_name, "r")
for eachline in file1:
    eachline = eachline.rstrip()
    student_marks = eachline.split(" - ")
    print(student_marks)
    student_list[student_marks[0]] = student_marks[1]
    print(student_list)
file1.close()
"""""
file1_name = sys.argv[2]
file1_name = open(file1_name, "r")
for eachstudent in student_list.keys():
    print(eachstudent, student_list[eachstudent])
file1_name.close()

    if student_list < 40:
        print(student_marks)
        print("better luck next time")"""
