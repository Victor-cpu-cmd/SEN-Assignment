# Student Result Management System (SRMS)

class ResultManager:
    def __init__(self):
        self.students = []

    def calculate_grade(self, score):
        if score >= 70:
            return "A"
        elif score >= 60:
            return "B"
        elif score >= 50:
            return "C"
        elif score >= 45:
            return "D"
        else:
            return "F"

    def add_student(self, name, score):
        grade = self.calculate_grade(score)
        student = {
            "name": name,
            "score": score,
            "grade": grade
        }
        self.students.append(student)
        print("Student added successfully!\n")

    def display_results(self):
        if not self.students:
            print("No student records found.\n")
            return
        print("\n--- Student Results ---")
        for student in self.students:
            print(f"Name: {student['name']}, Score: {student['score']}, Grade: {student['grade']}")
        print()

def main():
    manager = ResultManager()

    while True:
        print("Student Result Management System (SRMS)")
        print("1. Add Student")
        print("2. Display Results")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            score = int(input("Enter student score: "))
            manager.add_student(name, score)

        elif choice == "2":
            manager.display_results()

        elif choice == "3":
            print("Exiting SRMS...")
            break

        else:
            print("Invalid option! Try again.\n")

if __name__ == "__main__":
    main()
