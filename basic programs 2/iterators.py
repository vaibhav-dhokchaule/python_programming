# Return an iterator from a tuple.
# mytuple=("apple",'banana',"cherry")
# iterator=iter(mytuple)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Return an iterator from a string.
# mystring = "Vaibhav"
# iterator = iter(mystring)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Loop through an iterator.
# tuple = ("apple","banana","cherry")
# for x in tuple :
#     print(x)


# Create an iterator..
# class MyNumber:
#     def __iter__(self):
#         self.a = 1
#         return self
#     def __next__(self):
#         x = self.a
#         self.a +=1
#         return x
# myclass = MyNumber()
# iterator = iter(myclass)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Stop iteration.
class MyNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a +=1
            return x
        else:
            raise StopIteration

myclass = MyNumber()
iterator=iter(myclass)

for x in iterator:
    print(x)


    
