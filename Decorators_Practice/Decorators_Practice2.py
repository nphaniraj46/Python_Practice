def add(a,b):  #here iam doing this doing some changes in this function using decorator
    return a+b
f=add #if we make some chnages in this the original function is pointing to this new function which is inside this decorator which is inner
#so iam saving this referance in this varibale this f variable acts as this old add function which does this a+b

def decorator(func): #This is the decorator we need pass a function refrence to this decorator 
    def inner(a,b): #This is where the main part here we can make some changes like i have done a-b which ealrier function has this a+b
        return a-b
    return inner

add=decorator(add)

new_Function=add(1,2) #iam calling this new fucntion which has latest operation which we have updated this a+b to a-b
old_Function=f(1,2) #iam calling this old function using the reference which we saved earlier

print(new_Function) #and here iam printing the results of old and new functions dude
print(old_Function)

