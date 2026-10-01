#declare variables
expense_list = []
expense = 1 
small_expenses = float
moderate_expenses = float
large_expenses = float
small_expenses = 0
moderate_expenses = 0
large_expenses = 0

#repeatedly ask user for input until they enter "0"
while expense != 0:
    expense = float(input("Enter expense here or type 0 to finish: "))

#don't let user enter negative number
    if expense < 0:
        print("Expense can't be negative, try again: ")

#get and store number of small, moderate, and large expenses
    elif expense != 0:
        if expense < 25:
            small_expenses = small_expenses + 1
        elif expense >= 25 and expense <= 100:
            moderate_expenses = moderate_expenses + 1
        elif expense > 100:
            large_expenses = large_expenses + 1

        expense_list.append(expense)

#calculations
total_num_expenses = float(len(expense_list))
total_expenses = float(sum(expense_list))
avg_expenses = total_expenses/total_num_expenses
smallest_expense = float(min(expense_list))
largest_expense = float(max(expense_list))

#print out results
print("Summary of Total Expenses\n")
print(f"Number of Expenses:{total_num_expenses}")
print("Total: " f"${total_expenses:,.2f} ")
print("Average: " f"${avg_expenses:,.2f} ")
print("Smallest: " f"${smallest_expense:,.2f} ")
print("Largest: " f"${largest_expense:,.2f} ")

#print number of each expense
print(f"Small Expenses: {small_expenses}")
print(f"Moderate Expenses: {moderate_expenses}")
print(f"Large Expenses: {large_expenses}\n")
