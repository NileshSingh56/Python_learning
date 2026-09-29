#Expense tracker project

expenses=[]

print("Welcome to expense tracker!")
while True:
    print("=========Menu=========")
    print("1. Add expense")
    print("2. View all expenses")
    print("3. View total expenses")
    print("4. Exit")
    choice=int(input("Enter your choice (1-4): "))

    if choice==1:
        date=input("Enter the date (YYYY-MM-DD): ")
        category=input("Enter the category (e.g. food, transportation, entertainment): ")
        description=input("Enter the description: ")
        amount=float(input("Enter the amount: "))

        expense={
            "date":date,
            "category":category,
            "description":description,  
            "amount":amount

        }
        expenses.append(expense)
        print("Expense added successfully!")

    elif choice==2:
        if len(expenses)==0:
            print("No expenses done.")
        else:
            print("All expenses")
            count=1
            for each in expenses:
                print(f"{count}. {each['date']}, {each['category']}, {each['description']}, {each['amount']}")
                count+=1
    elif choice==3:
        total=0
        for each in expenses:
            total+=each["amount"]
        print(f"Total expenses: {total}")
    elif choice==4:
        print("Exiting the program. Goodbye!")
        break