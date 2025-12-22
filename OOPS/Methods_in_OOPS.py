class bank:
    bank_name="SBI" #this is a calss variable shared across all objects
    def __init__(self,name,age):
        """
        Instance Method
         Initializes instance variables specific to each objectx`
        """
        self.name=name #this is instance variable
        self.age=age #this is also a instance variable
    def info(self): #this is the instance method
        print(f"Name of the person is {self.name} and age is {self.age} your bank is {bank.bank_name}\n")
    @classmethod
    def change_bank_name(cls,new_bank_name):#This is calss method
        """
        Used to modify the class variable for all objects.
        """
        cls.bank_name=new_bank_name
    @staticmethod
    def bank_policy():
        """
         Static Method
          General information method does not depend on instance or class variables
        """
        print("All account holders must maintain a minimum balance of 1000.\n")

p1=bank("Phani",22)
p1.info()
bank.change_bank_name("Union") # Changing bank name using class method
p2=bank("nRaj",23)
p2.info()
# Calling static method
bank.bank_policy() 