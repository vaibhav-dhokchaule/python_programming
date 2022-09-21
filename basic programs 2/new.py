row = int(input("Enter the number of rows:"))  
column = int(input("Enter the number of columns:"))  
# print("*"*column)
matrix = [[int(input()) for x in range (column)] for y in range(row)]  
print(matrix)  