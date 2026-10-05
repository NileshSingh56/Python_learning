#Write a program to read a text from a given file certificate.txt and find whether it contains the word live.

file=open("certificate.txt","r")
dataOfFile=file.read()

dataOfFile=dataOfFile.lower()
if "live" in dataOfFile:
    print("Yes ,live word is present in the file")
else:
    print("No, live word is not present in the file")
file.close()

