# Task is to read only the first line of bio.txt

with open("bio.txt","r") as file:
    Line1=file.readline()
    print("First line of the file is:",Line1)