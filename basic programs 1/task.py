array = []
print("\n")
n = int(input("Enter the no. of rows: "))
print("\n")
i=0
while i < n:
    print("Enter number of stars:" )
    i+=1
    item = int(input())
    array.append(item)
    s= print("*"*item)
print("The Star pattern is:\n")
for i in range(0,n):
    for j in range(0,i+1):
         print("*")
         
# for i in range(n):
    #  print("*")


# print("User list is ", array)

