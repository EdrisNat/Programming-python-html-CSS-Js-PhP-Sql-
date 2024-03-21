class Person:
    def __init__(self, name):
        # Constructor to initialize a Person object with a name
        self._name = name  # Private attribute to store the person's name

    def get_name(self):
        # Method to get the person's name
        return self._name

    def set_name(self, name):
        # Method to set the person's name
        self._name = name


class Teacher(Person):
    def __init__(self, name):
        # Constructor to initialize a Teacher object with a name
        super().__init__(name)
        self._courses_taught = []  # List to store courses taught by the teacher

    def teach_course(self, course):
        # Method to assign a course to the teacher
        self._courses_taught.append(course)

    def get_courses_taught(self):
        # Method to get the list of courses taught by the teacher
        return self._courses_taught


class Student(Person):
    def __init__(self, name, grade_level):
        # Constructor to initialize a Student object with a name and grade level
        super().__init__(name)
        self._grade_level = grade_level  # Grade level of the student

    def get_grade_level(self):
        # Method to get the grade level of the student
        return self._grade_level

    def set_grade_level(self, grade_level):
        # Method to set the grade level of the student
        self._grade_level = grade_level


class Course:
    def __init__(self, name, department, teacher):
        # Constructor to initialize a Course object with a name, department, and teacher
        self._name = name  # Name of the course
        self._department = department  # Department offering the course
        self._teacher = teacher  # Teacher assigned to the course
        self._students_enrolled = []  # List to store students enrolled in the course

    def enroll_student(self, student):
        # Method to enroll a student in the course
        self._students_enrolled.append(student)

    def get_students_enrolled(self):
        # Method to get the list of students enrolled in the course
        return self._students_enrolled

    def get_teacher(self):
        # Method to get the teacher assigned to the course
        return self._teacher


class Department:
    def __init__(self, name, school):
        # Constructor to initialize a Department object with a name and school
        self._name = name  # Name of the department
        self._school = school  # School to which the department belongs
        self._courses = []  # List to store courses offered by the department

    def add_course(self, course):
        # Method to add a course to the department
        self._courses.append(course)

    def get_courses(self):
        # Method to get the list of courses offered by the department
        return self._courses


class School:
    def __init__(self, name):
        # Constructor to initialize a School object with a name
        self._name = name  # Name of the school
        self._departments = []  # List to store departments of the school

    def add_department(self, department):
        # Method to add a department to the school
        self._departments.append(department)

    def get_departments(self):
        # Method to get the list of departments of the school
        return self._departments


# Testing the implementation
if __name__ == "__main__":
    # Create School
    my_school = School("XYZ School")

    # Create Departments
    math_department = Department("Mathematics", my_school)
    physics_department = Department("Physics", my_school)

    # Add Departments to School
    my_school.add_department(math_department)
    my_school.add_department(physics_department)

    # Create Teachers
    math_teacher = Teacher("John Doe")
    physics_teacher = Teacher("Jane Smith")

    # Assign Teachers to Departments
    math_department.add_course(Course("Algebra", math_department, math_teacher))
    physics_department.add_course(Course("Physics 101", physics_department, physics_teacher))

    # Create Students
    student1 = Student("Alice", 10)
    student2 = Student("Bob", 11)

    # Enroll Students in Courses
    algebra_course = math_department.get_courses()[0]
    physics_course = physics_department.get_courses()[0]
    algebra_course.enroll_student(student1)
    physics_course.enroll_student(student2)

    # Display Course Information
    print(f"Course: {algebra_course._name}, \nTeacher: {algebra_course.get_teacher().get_name()}")
    print("Students Enrolled:")
    for student in algebra_course.get_students_enrolled():
        print(student.get_name())

    print(f"\nCourse: {physics_course._name},\nTeacher: {physics_course.get_teacher().get_name()}")
    print("Students Enrolled:")
    for student in physics_course.get_students_enrolled():
        print(student.get_name())
