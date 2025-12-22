#lets say if i have a function that which is doing divison of two number


def decorator(func):#here this decorators takes this functions as the input this is like a function that takes a function
    def inner(a,b):#here the magic happens the we can do modification of the div functions or any function we are goin to use 
        if a<b:
            a,b=b,a #here iam swapping a variable if a<b
            return func(a,b) 
    return inner #here i need to reutn this inner to this decorator function

@decorator
def div(a,b): #This function works well but if i need to add some conditions like i need to swap two vlaues if a<b for this one we can use this decoratos
    return a/b

division=div(2,4)
print(division) 