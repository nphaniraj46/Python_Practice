class computer:
    brand='HP'#Here this is class variable we can use this though out this class associated with this classname for example if we need to call this class variable we can use this as compter.brand
    def __init__(self,processor,storage,ram):
        print("Init is called") #This in it constructor is exceuted when we create a new object 
        #in this clase we created only one object so in output we will get this this Init called only one time
        self.processor=processor
        self.storage=storage
        self.ram=ram
    def LaptopDetails(self):
        print(f"Yor {computer.brand} is have this processor {self.processor} and storage of {self.storage} with that ram {self.ram}") #here i used this class variable inside a method of class using classname.variable name

com1=computer("Ryzen 5600H","512 GB","16GB")
com1.LaptopDetails() #this can be written as computer.LaptoopDetails(com1)

print(computer.brand)
        