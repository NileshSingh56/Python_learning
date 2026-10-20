N=int(input("Enter a number to get the sum of even numbers: "))
sum=0
i=N
while i>=1:
    if i%2==0:
        sum=sum+i
    i=i-1
print(f'The sum of even numbers from {N} to 1 is: {sum}')