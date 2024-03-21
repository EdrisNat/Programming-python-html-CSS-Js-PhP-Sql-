class Employee:
    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, base_salary, bonus):
        self.base_salary = base_salary
        self.bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.bonus


class Developer(Employee):
    def __init__(self, hourly_rate, hours_worked):
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked


# Create instances of Manager and Developer
manager = Manager(5000, 2000)
developer = Developer(50, 160)

# Create a list of employees
employees = [manager, developer]

# Iterate over the list and call calculate_salary() method for each object
for employee in employees:
    print("Salary for {}: ${}".format(employee.__class__.__name__, employee.calculate_salary()))
