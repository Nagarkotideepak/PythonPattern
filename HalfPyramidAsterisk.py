rows= int (input("Enter Number of rows to print * Half Pyramid: "))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=' ')
    print("\r")
