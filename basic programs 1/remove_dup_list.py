mylist = ["a", "b", "a", "c", "c"]   #a list some duplicate element
mylist = list(dict.fromkeys(mylist))  
                     #Create a dictionary, using the List items as keys.
                     #  This will automatically remove any duplicates 
                     # because dictionaries cannot have duplicate keys.

                    #  Then, convert the dictionary back into a list:
print(mylist)       #Print the List to demonstrate the result



#OR
#  def my_function(x):
#   return list(dict.fromkeys(x))

# mylist = my_function(["a", "b", "a", "c", "c"])

# print(mylist)
