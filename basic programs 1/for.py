# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:19:11 2022

@author: vaibh
"""

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 



# for loop for a string items

for x in "vaibhav":
  print(x)
  
  
  # Exit the loop when x in banana
  
fruits=["mango","cherry","banana","orange"]
for x in fruits:
    print(x)
    if x=="banana":
      break
  
    
  
  # break the loop but break comes brfore th banana 
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


# continue statment - for loop

fruits=["mango","pineapple","cherry","orange","banana"]
for x in fruits:
    if x == "cherry":
        continue
    print(x)