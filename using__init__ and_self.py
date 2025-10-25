class car:
    def __init__(self,brand,model):
        #This init constructor excecutes automatically when we create an object
        self.brand=brand
        self.model=model
    def info(self):
        print(f"{self.brand},{self.model}")
c1=car("Lambo","Urus")
c1.info()
c2=car("BMW","XN")
c2.info()