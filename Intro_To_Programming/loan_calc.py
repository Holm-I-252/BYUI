loan_size = int(input("Enter the size of the loan from 1-10: "))
credit_history = int(input("Enter the credit history from 1-10: "))
income = int(input("Enter the income from 1-10: "))
down_payment = int(input("Enter the down payment from 1-10: "))

loan_given = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        loan_given = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            loan_given = True

elif loan_size < 5:
    if credit_history >= 4:
        loan_given = True
    else:
        if income >= 7 or down_payment >= 7:
            loan_given = True
        elif income >= 4 and down_payment >= 4:
            loan_given = True
        

if loan_given:
    print("Loan approved!")
else:
    print("Loan denied.")