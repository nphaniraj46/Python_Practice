#in this i have learned how to create a class object and objects


class car:
    def start_engine(self):       
        """
        This method prints a message when the car engine starts.
        'self' refers to the current object calling this method.
        """
      print("Engine stared man lets goo!!!")
c1=car()
c1.start_engine() 
#we can also write this as car().start_engine(c1) Hrer the self is being replaced with the object