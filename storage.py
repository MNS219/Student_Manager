FILE = "data.txt"

def save_student(student):
    with open(FILE, "a") as f:
        f.write(str(student) + "\n")

def get_students():
    with open(FILE, "r") as f:
        return f.readlines()
    
def delete_student(roll):
    students = get_students()
    new = [s for s in students if not s.startswith(roll)]
    open(FILE, "w").writelines(new)