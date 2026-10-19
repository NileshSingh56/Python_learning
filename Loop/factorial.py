a=int(input("Enter a number to get its factorial: "))
factorial=1
for i in range(1,a+1,1):
    factorial=factorial*i
print(f'The factorial of {a} is: {factorial}')