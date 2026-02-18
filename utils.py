def print_menu():
    print("===== STUDENT MANAGER =====")
    print("1. Add Student")
    print("2. View Students")

def export_csv():
    import shutil
    shutil.copy("data.txt", "students_backup.csv")
    print("Data exported to students_backup.csv")