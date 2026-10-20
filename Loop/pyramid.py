a=int(input("Enter first number: "))
for i in range(1, a + 1):
    row="" 
    for j in range(1,a-i+1):
        row=row+" "
    for k in range(1,i+1):
        row=row+"* "
    print(row)