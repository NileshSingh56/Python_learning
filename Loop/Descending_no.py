a=int(input("Enter first number: "))
for i in range(1,a+1):
    row=""
    for j in range(i,0,-1):
        row += str(j)
    print(row)