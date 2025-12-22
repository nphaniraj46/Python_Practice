class Laptop:
    def details(self,brand,ram):
        self.brand=brand
        self.ram=ram
        print(f"Hey Your laptops brand is {self.brand} and Ram is {self.ram}")
l1=Laptop()
l2=Laptop()

l1.details("HP",16)
l2.details("Dell",16)
        