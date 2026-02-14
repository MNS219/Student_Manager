class Student:
    def __init__(self, roll, name, dept):
        self.roll = roll
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.roll},{self.name},{self.dept}"