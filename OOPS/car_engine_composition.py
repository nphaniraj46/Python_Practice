class Engine():
    def start(self):
        print("Engine Started")
class car():
    def __init__(self):
        self.engine=Engine() #here iam just creating a object inside this init method of this car class with this object we can access this methods of this engine class as well this is very intresting this is aslo know as composition

    def drive(self):
        self.engine.start() #here iam calling engine class using the object we created in this car class
        print("Car is moving")

car1=car()

car1.drive()