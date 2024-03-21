# parent class
class user:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


    def view_detail(self):
        print(" ")
        print(f"Name:{self.name}")
        print(f"Age:{self.age}")
        print(f"Gender:{self.gender}")

# child class
class bank(user):
    def __init__(self, name, age, gender):
        super(). __init__(name,age,gender)
        self.balance = 0

    def deposit(self,amount):
        self.amount = amount
        self.balance =self.balance + self.amount
        print("Account balance is:$", {self.balance})

    def withdraw(self, amount):
        self.amount = amount
        if amount > self.balance:
            print("Insufficient Funds | balance available: $", {self.balance})
        else:
            self.balance = self.balance - self.amount
            print("Account balance has been updated after $200 withdraw and balance is : $", {self.balance})
    def view_balance(self):
        self.view_detail()
        print("Account balance: $ ", {self.balance})

#usage
bank_user = bank("Edris", 30, "Male")
bank_user.view_detail()
bank_user.deposit(3000)
bank_user.withdraw(200)
bank_user.view_balance()