# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 16:30:45 2022

@author: vaibh
"""

def my_function():
  print("hello , welcome to python function...")
  
my_function()    # calling a function





def my_function(lname):
    print(lname + "Dhokchaule")
    
my_function("vaibhav ")
my_function("pratik ")
my_function("mangesh ")
my_function("rohan ")




def my_function(fname,lname):
    print(fname+ " " + lname)
    
my_function("vaibhav","dhokchaule")



# If you do not know how many keyword arguments that will 
# be passed into your function, add two asterisk: * before
# the parameter name in the function definition.


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("vaibhav", "shubham", "ashish")




def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "vaibhav", child2 = "shubham", child3 = "ashish")




# If you do not know how many keyword arguments that will 
# be passed into your function, add two asterisk: * before
# the parameter name in the function definition.    

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "vaibhav", lname = "dhokchaule")



# If we call the function without argument, it uses the default value:
    
    
def my_function(country = "Norway"):
  print("I am from " + country)

my_function("london")
my_function("India")
my_function()
my_function("Brazil")



def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


