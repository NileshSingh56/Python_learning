a=int(input("Enter the number of rows for the alphabet pattern: "))
for i in range(1,a+1):
    char=str(chr(64+i))
    output=char* i
    print(output)