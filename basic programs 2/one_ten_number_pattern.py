current_Number = 1  
stop = 2  
rows = 3  # Number of rows to print numbers  
  
for i in range(rows):  
    for j in range(1, stop):  
        print(current_Number, end=' ')  
        current_Number += 1  
    print("")  
    stop += 2  