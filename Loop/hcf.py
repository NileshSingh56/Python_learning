a = abs(int(input("Enter first number: ")))
b = abs(int(input("Enter second number: ")))

if a == 0 and b == 0:
    print("HCF is undefined for 0 and 0")
else:
    while b != 0:
        a, b = b, a % b

    print("HCF is:", a)