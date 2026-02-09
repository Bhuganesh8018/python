student_roll =(19001, 19002, 19003)
student_name = ("raj", "hari", "vineet")
student=dict(zip(student_roll, student_name))
print("Existing student dictionary")
print(student)

roll_no=int(input("enter roll no: "))
name= input("enter the student name: ")
student[student_roll] = name

print("\nUpdated student dictionary: ")
print(student)
