from datetime import date

class Person:
    def __init__(self, first_name, last_name, phone_number, date_of_birth):
        self._first_name = first_name
        self._last_name = last_name
        self._phone_number = phone_number
        self._date_of_birth = date_of_birth
        self._addresses = []

    def add_address(self, address):
        self._addresses.append(address)

class Address:
    def __init__(self, id, country, city, street, postal):
        self._id = id
        self._country = country
        self._city = city
        self._street = street
        self._postal = postal

class Employee(Person):
    def __init__(self, id, first_name, last_name, phone_number, date_of_birth, title, international, date_of_employment):
        super().__init__(first_name, last_name, phone_number, date_of_birth)
        self._id = id
        self._title = title
        self._international = international
        self._date_of_employment = date_of_employment
        self._enrollments = []

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

    def is_part_time(self):
        return False

    def is_on_probation(self):
        return False

class Trainer(Person):
    def __init__(self, id, first_name, last_name, phone_number, date_of_birth, domain, salary):
        super().__init__(first_name, last_name, phone_number, date_of_birth)
        self._id = id
        self._domain = domain
        self._salary = salary
        self._courses = []

    def check_for_raise(self):
        return False

    def add_course(self, course):
        self._courses.append(course)

class Course:
    def __init__(self, name, code, max_students, min_students):
        self._name = name
        self._code = code
        self._max_students = max_students
        self._min_students = min_students
        self._trainers = []
        self._enrollments = []

    def add_trainer(self, trainer):
        self._trainers.append(trainer)

    def add_enrollment(self, enrollment):
        self._enrollments.append(enrollment)

    def is_cancelled(self):
        return False

class Enrollment:
    def __init__(self, employee, course, grade=None, enrollment_date=None):
        self._employee = employee
        self._course = course
        self._grade = grade
        self._enrollment_date = enrollment_date

    def set_grade(self, grade):
        self._grade = grade

#Selecting a choice
print("Welcome to the MIS please make as selection:\n")
choice = input("Employee(E) or a Trainer(T): ")

if choice == "Employee" or choice.upper() == "E":
    # Input for creating an employee
    employee_id = input("Enter Employee ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    title = input("Enter Title: ")
    international = input("Is International (True/False): ")
    date_of_employment = input("Enter Date of Employment (YYYY-MM-DD): ")

    employee1 = Employee(employee_id, first_name, last_name, phone_number, date_of_birth, title, international, date_of_employment)


    # Input for employee address
    address_id = input("Enter Address ID: ")
    country = input("Enter Country: ")
    city = input("Enter City: ")
    street = input("Enter Street: ")
    postal = input("Enter Postal Code: ")

    address1 = Address(address_id, country, city, street, postal)
    employee1.add_address(address1)

    # Output
    print("\nEmployee Information")
    print(f"Employee_ID: {employee1._id}")
    print(f"Name: {employee1._first_name} {employee1._last_name}")
    print(f"Title: {employee1._title}")
    print(f"International: {employee1._international}")
    print(f"Date of Employment: {employee1._date_of_employment}")
    print(f"Is Part Time: {employee1.is_part_time()}")
    print(f"Is on Probation: {employee1.is_on_probation()}")
    print("Employee Address:")
    for address in employee1._addresses:
        print(f"{address._street}, {address._city}, {address._country}, {address._postal}")

elif choice == "Trainer" or choice.upper() == "T":
    trainer_id = input("Enter Trainer ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    phone_number = input("Enter Phone Number: ")
    date_of_birth = input("Enter Date of Birth (YYYY-MM-DD): ")
    domain = input("Enter Domain: ")
    salary = input("Enter Salary: ")

    trainer = Trainer(trainer_id, first_name, last_name, phone_number, date_of_birth, domain, salary)

    # Input for trainer address
    address_id = input("Enter Address ID: ")
    country = input("Enter Country: ")
    city = input("Enter City: ")
    street = input("Enter Street: ")
    postal = input("Enter Postal Code: ")

    address = Address(address_id, country, city, street, postal)
    trainer.add_address(address)

    #Output for trainer
    print("\nTrainer Information")
    print(f"Trainer_ID: {trainer._id}")
    print(f"Name: {trainer._first_name} {trainer._last_name}")
    print(f"Domain: {trainer._domain}")
    print(f"Salary: ${trainer._salary}")
    print(f"Received Raise: {trainer.check_for_raise()}")
    print("Trainer Address:")
    for address in trainer._addresses:
        print(f"{address._street}, {address._city}, {address._country}, {address._postal}")

else:
    print("Invalid choice. Try again")