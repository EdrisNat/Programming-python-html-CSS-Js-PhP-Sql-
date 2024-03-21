# Define a class to represent a Student
class Student:
    # Constructor method to initialize student attributes: name, age, grade
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Method to provide a string representation of a Student object
    def __repr__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

# Define a class to represent a Course
class Course:
    # Constructor method to initialize course attributes: name, max_students
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []  # Initialize an empty list to store enrolled students

    # Method to add a student to the course
    def add_student(self, student):
        # Check if the course has reached its maximum capacity
        if len(self.students) < self.max_students:
            self.students.append(student)  # Add the student to the list of enrolled students
            return True  # Return True indicating successful enrollment
        return False  # Return False indicating failed enrollment due to course being full

    # Method to provide a string representation of a Course object
    def __repr__(self):
        return f"Course: {self.name}, Students: {self.students}, Max Students: {self.max_students}"

# Define a class to represent a School
class School:
    # Constructor method to initialize school attributes: students, courses
    def __init__(self):
        self.students = []  # Initialize an empty list to store students
        self.courses = []   # Initialize an empty list to store courses

    # Method to add a student to the school
    def add_student(self, student):
        self.students.append(student)  # Add the student to the list of students in the school

    # Method to add a course to the school
    def add_course(self, course):
        self.courses.append(course)  # Add the course to the list of courses in the school

    # Method to enroll a student in a course
    def enroll_student(self, student_name, course_name):
        # Search for the student in the list of students
        student = next((s for s in self.students if s.name == student_name), None)
        # Search for the course in the list of courses
        course = next((c for c in self.courses if c.name == course_name), None)

        # Check if both student and course exist
        if student and course:
            # Attempt to add the student to the course
            if course.add_student(student):
                return f"{student_name} enrolled in {course_name}"  # Return success message
            else:
                return f"Failed to enroll {student_name} in {course_name}. Course is full."  # Return failure message
        else:
            return "Student or course not found."  # Return message indicating student or course not found

    # Method to provide a string representation of a School object
    def __repr__(self):
        return f"School: Students: {self.students}, Courses: {self.courses}"


# Example usage:
school = School()  # Instantiate a School object

# Create students
student1 = Student("Alice", 15, 10)  # Instantiate a Student object
student2 = Student("Bob", 16, 11)     # Instantiate another Student object

# Add students to school
school.add_student(student1)  # Add student1 to the school
school.add_student(student2)  # Add student2 to the school

# Create courses
course1 = Course("Math", 2)      # Instantiate a Course object
course2 = Course("English", 1)   # Instantiate another Course object

# Add courses to school
school.add_course(course1)  # Add course1 to the school
school.add_course(course2)  # Add course2 to the school

# Enroll students in courses
print(school.enroll_student("Alice", "Math"))    # Should be successful
print(school.enroll_student("Bob", "Math"))      # Should be successful
print(school.enroll_student("Alice", "English")) # Should fail because course is full

print(school)  # Print the school object to see its current state

