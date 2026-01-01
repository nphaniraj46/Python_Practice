#This encapsulation menas we are not able to use the varibales that are privated using __ (double undersocre)
#We can only access this privated variable with the methods only we are not able to call them using object

class BankAccount:
    bank_name = "SBI"

    def __init__(self, name, accno, balance):
        self.name = name
        self.accno = accno
        self.__balance = balance   #private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Balance:", self.__balance)

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount #updating the balance here
            print("Withdraw successful")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

c1=BankAccount("Phani",123,500)

print(c1.__balance) #here iam trying to access we will get error because this balance is a private variable