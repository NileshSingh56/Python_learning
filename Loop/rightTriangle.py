a=int(input("Enter a value to get the right triangle: "))
for i in range(1,a+1):
    row=""
    for j in range(1,i+1):
        row=row+"*"
    print(row)