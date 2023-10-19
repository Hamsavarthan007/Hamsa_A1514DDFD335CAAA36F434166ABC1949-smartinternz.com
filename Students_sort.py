class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Initialize an empty list to store student objects
student_list = []

# Get user input for student data
while True:
    name = input("Enter student's name (or type 'done' to finish): ")
    if name.lower() == 'done':
        break
    roll_number = input("Enter student's roll number: ")
    cgpa = float(input("Enter student's CGPA: "))
    
    student = Student(name, roll_number, cgpa)
    student_list.append(student)

# Check if there are students in the list
if len(student_list) > 0:
    # Sort the list of students by CGPA in descending order
    sorted_students = sort_students(student_list)

    # Print the sorted list of students
    print("\nSorted List of Students:")
    for student in sorted_students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
else:
    print("No student data entered.")
