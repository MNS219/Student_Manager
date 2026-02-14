FILE = "data.txt"

def save_student(student):
    with open(FILE, "a") as f:
        f.write(str(student) + "\n")

def get_students():
    with open(FILE, "r") as f:
        return f.readlines()