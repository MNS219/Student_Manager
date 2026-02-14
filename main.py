from student import Student
from storage import save_student, get_students
from utils import print_menu

def add_student():
    roll = input("Roll: ")
    name = input("Name: ")
    dept = input("Dept: ")
    s = Student(roll, name, dept)
    save_student(s)

def view_students():
    students = get_students()
    for s in students:
        print(s.strip())

print_menu()
choice = input("Enter choice: ")

if choice == "1":
    add_student()
elif choice == "2":
    view_students()