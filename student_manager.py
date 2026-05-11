# 🎓 Student Result Manager

students = {}

def add_student():
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))
    students[name] = marks
    print(f"✅ {name} added successfully!\n")

def view_students():
    if not students:
        print("⚠️ No students found.\n")
        return
    
    print("\n📋 Student List:")
    for name, marks in students.items():
        print(f"{name} → {marks}")
    print()

def find_topper():
    if not students:
        print("⚠️ No data available.\n")
        return
    
    topper = max(students, key=students.get)
    print(f"🏆 Topper: {topper} ({students[topper]} marks)\n")

def main():
    while True:
        print("===== Student Manager =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Find Topper")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            find_topper()
        elif choice == "4":
            print("👋 Exiting program...")
            break
        else:
            print("❌ Invalid choice!\n")

if __name__ == "__main__":
    main()