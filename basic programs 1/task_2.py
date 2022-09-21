row = int(input("Enter the number of rows:"))  
column = int(input("Enter the number of columns:"))  
  
# Initialize matrix  
matrix = []  
print("Enter the no. of stars row-wise:")  
  
# For user input  
for i in range(row):         # A for loop for row entries  
    a =[]  
    for j in range(column):  # A for loop for column entries  
        a.append(int(input()))  
    matrix.append(a)  
  
# For printing the matrix  
for i in range(row):  
    for j in range(column):  
        print(matrix[i][j], end = " ")  
    print()  