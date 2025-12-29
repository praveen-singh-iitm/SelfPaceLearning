students={
    "Alice":98,
    "Mark":55,
    "Adam":67,
    "Bob":86
}


student_name=input("Enter the student's name : ")

if students.get(student_name):
    print(f"{student_name}'s mark : {students[student_name]}")
else:
    print(f"Student not found")