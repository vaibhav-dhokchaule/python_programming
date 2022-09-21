'''
n = int(input("Enter the number of rows :"))
for i in range(0,n):
    for j in range(0,n):
        print("*",end=" ")
    n = n-1 
    print()

'''

'''

r1=int(input("Enter the no.of stars in first row:"))
print("*"*r1)
r2=int(input("Enter the no.of stars in second row:"))
print("*"*r2)
r3=int(input("Enter the no.of stars in third row:"))
print("*"*r3)
r4=int(input("Enter the no.of stars in fourth row:"))
print("*"*r4)
r5=int(input("Enter the no.of stars in fifth row:"))
print("*"*r5)

'''


'''
n = int(input("Enter the number of rows:"))
# print("Enter the stars:\n"*n )
rows = int(input("Enter the number of stars:"))
print("*"*rows)
#   n.append(rows)
#   print("*"*rows)
'''

a = []
print("\n")
n = int(input("Enter the no. of rows:"))
print("\n")
i=0
while i < n:
    # print("Enter number of stars:" )
    i+=1
    item = int(input("Enter number of stars:"))
    a.append(item)
    print("*"*item)
print("The star pattern is:\n")
for i in range(0,item):             # equal rows equal no.of stars
    print("*"*item)
# 1 to n pattern print
# for i in range(1,n+1):
#     print("*"*i)














# for i in range(n):
#    for j in range(item):

# for n in range( 0, n+1 ):
#   for item in range(1,n+1):
    # print("*",end=" ")
#   print() 






# for i in range(item):
    #  print("*"*item)
# print("User list is ", array)



'''
n= int(input("Enter the number of rows:"))
if n in range(0,n):
  print(n)
m=int (input("Enter the number of stars:"))
print("*"*m)

'''




# print("Enter the number of stars: ", n)  
# print("Enter the number of stars:", n)  
# print("Enter the number of stars:", n)  
# print()  

   




'''
list1=[]

for i in range(5):

  x=int(input("enter the number:" ))

list1.append(x)

print(list1)

'''









# for n in range(0)
# print("*"*rows)



































'''
r1=r2=r3=r4=r5=int(input("Enter the no.of stars:"))
print("*"*r1)
print("*"*r2)
print("*"*r3)
print("*"*r4)
print("*"*r5)

'''


'''
for i in range(1,9):
    for j in range(1,9):
        if j<= 9-i:
            print("*", end='')
        else:
            print("",end='')
    print()


'''


'''
for i in range(5,0,-1):
    for k in range(1,6-i):
        print(" ",end=" ")
    for j in range(1,(2*i-1)+1):
     print("*",end="")
    print("\n")
'''


'''
for row in range( 1, rows+1 ):
  for col in range(1,row+1):
     print("*",end=" ")
  print()
'''

'''
for row in range(rows-1, 0,-1):
    for col in range(1,row+1):
        print("*",end="")
    print()

    '''


 