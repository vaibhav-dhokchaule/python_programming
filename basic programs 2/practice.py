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

    for k in range(0,item):
        pattern=print("The pattern is")
print("*"*item)

'''

n = int(input("Enter the number of rows:"))
rows=int(input("Enter the number of stars:"))
for i in range(rows):
    i=0
    if i<=n:
        i+=1
        print("*"*rows)
# if rows<=n:
#     rows+=1
#     .append(rows)
#     print("*"*rows)






















# print("The star pattern is:\n")
# for i in range(item):
# #    for j in range(item):
#     print("*"*n)