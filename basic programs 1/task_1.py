

n = int(input("Enter the number of rows: "))  
for i in range(n + 1, 0, -1):
    # if i<=1:
        # print("*"*(n-4))
    # print(" ")

    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")  




















'''

n = int(input("Enter the number of rows :"))
for i in range(0,n):
     if i< n-4:
         print("*",end=" ")
  if i<=1 or i>=0 :
    print("*"*(n-4))
    for j in range(0,n):
        print("*",end=" ")
    n = n-1 
    print()

'''



'''
rows = 9
for i in range(rows + 1, 0, -1):
    
    for j in range(0, i - 1):
      
        print("*", end=' ')
    print(" ")


'''








'''
n = int(input("Enter the number of rows:"))
for i in range(n):
    if(n==1) :
        print("*"*(n-4))
    else:
        print("*"*(n-i))

'''



'''
    n = int(input("Enter the number of rows :"))
    for i in range(0,5):
       print("*",end=" ")

'''





