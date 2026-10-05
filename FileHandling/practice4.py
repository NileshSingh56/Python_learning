#Task is to print how many lines are present in notes.
with open("notes.txt","r") as file:
    data=file.readlines()
    print("Total number of lines in notes.txt is:",len(data))