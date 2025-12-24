class Employee():
    company="Google"
    def __init__(self,name):
        self.name=name

e1=Employee("Phani")
e2=Employee("raj")
e1.company="Meta" #This will not update this class variable here just another instance variable called company is created for this object e1

print(e2.company) #here we can access this class varibale with obkect and as well as this object name like objectname.class variable and classname.classvariable 