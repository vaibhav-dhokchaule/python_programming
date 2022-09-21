# how to create and call a function..
# def my_function():               # function defining
#   print("Hello function")
# my_function()              # function calling



# function parameter
# def my_function(lname):     # function parameter
#     print(lname + " dhokchaule")
# my_function("Vaibhav")
# my_function("Mangesh")
# my_function("Rohan")


# Default parameter value
# def my_function(country=" India"):
#     print("I'm from" + country )
# my_function(" America")
# my_function(" England")
# my_function()
# my_function(" taiwan")


# let function return a value.
# def my_function(x):
#     return 5 * x
# print(my_function(3))
# print(my_function(5))
# print(my_function(9)) 


# # Recursion
# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(result)
#   else:
#     result = 0
#   return result

# print("\n\nRecursion Example Results")
# tri_recursion(6)



def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
    
print("\n\n Recursion example result is: " )
tri_recursion(6)




