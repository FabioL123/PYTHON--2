# -------------------------------
# Student Node Class
# -------------------------------
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.next = None  # Pointer to the next node


# -------------------------------
# Singly Linked List Class
# -------------------------------
class StudentLinkedList:
    def __init__(self):
        self.head = None  # Start of the linked list

    # Add a student at the end of the list
    def add_student(self, student_id, name, grade):
        new_student = Student(student_id, name, grade)

        # If list is empty
        if self.head is None:
            self.head = new_student
            return

        # Traverse to the end
        current = self.head
        while current.next:
            current = current.next

        current.next = new_student

    # Search for a student by ID
    def search_student(self, student_id):
        current = self.head

        while current:
            if current.student_id == student_id:
                return current
            current = current.next

        return None

    # Delete a student by ID
    def delete_student(self, student_id):
        current = self.head
        previous = None

        while current:
            if current.student_id == student_id:
                # If deleting the head node
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True

            previous = current
            current = current.next

        return False

    # Display all students
    def display_students(self):
        if self.head is None:
            print("No student records available.")
            return

        current = self.head
        print("\nStudent Records:")
        print("----------------")
        while current:
            print(f"ID: {current.student_id} | Name: {current.name} | Grade: {current.grade}")
            current = current.next


# -------------------------------
# Main Program (Menu-Driven)
# -------------------------------
def main():
    student_list = StudentLinkedList()

    while True:
        print("\n===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Search Student by ID")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_id = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            grade = input("Enter Student Grade: ")
            student_list.add_student(student_id, name, grade)
            print("Student added successfully.")

        elif choice == "2":
            student_id = input("Enter Student ID to search: ")
            student = student_list.search_student(student_id)
            if student:
                print(f"Student Found -> ID: {student.student_id}, Name: {student.name}, Grade: {student.grade}")
            else:
                print("Student not found.")

        elif choice == "3":
            student_id = input("Enter Student ID to delete: ")
            if student_list.delete_student(student_id):
                print("Student deleted successfully.")
            else:
                print("Student not found.")

        elif choice == "4":
            student_list.display_students()

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 5.")


# Run the program
main()