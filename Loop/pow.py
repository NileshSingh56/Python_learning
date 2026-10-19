a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
pow=1
for i in range(1,b+1,1):
    pow=pow*a
print(f'{a} raised to the power {b} is: {pow}')