# create a class
# class Myclass:  //class creation
#     x = 5
# print(Myclass)


# create a object
# class Myclass:
#     x = 5
# p1 = Myclass()  //object creation
# print(p1.x)


# The __init__() function
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
# p1 = Person("Vaibhav",21)
# print(p1.name)
# print(p1.age)


# Create object method
# class Person:
#  def __init__(self,name,age):
#     self.name=name
#     self.age= age
#  def myfunc(self):
#     print("Hello my name is" + self.name)
# p1 = Person(" vaibhav",21)
# p1.myfunc()


# The self parameter
# class Person:
#     def __init__(me,name,age):
#         me.name=name
#         me.age=age
#     def myfunc(abc):
#         print("Hello , My name is" + abc.name)
# p1 = Person(" Vaibhav", 21)
# p1.myfunc()


# Modify the object property.
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def myfunc(self):
#         print("Hello My name is" +self.name)
# p1 = Person(" Vaibhav",21)
# p1.age = 40     //Modify object property
# print(p1.age)

# Delete Object Property.
# class Person:
#     def __init__(self,name,age):
#        self.name=name
#        self.age=age
#     def myfunc(self):
#         print("My name is" + self.name)
# p1 = Person(" Vaibhav", 21)
# del p1.age   //Delete object property
# print(p1.age)


# Delete Object
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        print("My name is " + self.name)
p1 = Person(" Vaibhav", 21)
del p1       #delete object  
print(p1)






