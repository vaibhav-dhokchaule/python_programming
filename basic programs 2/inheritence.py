# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 13:30:18 2022

@author: vaibh
"""

#parent class

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("vaibhav", "Dhokchaule")
x.printname()


#child class


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
        pass
        
x = Person("vaibhav","dhokchaule")
x.printname()
