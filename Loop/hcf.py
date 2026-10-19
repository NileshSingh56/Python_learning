a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
smaller=min(a,b)
hcf=1
for i in range(1,smaller+1,1):
    if a%i==0 and b%i==0:
        hcf=i
        break
print("HCF is:",hcf)
