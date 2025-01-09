accounts = []
balances = []

running = True
running_2 = False

while running:
    user_account = input("Enter an account name (Enter 'quit' to stop): ")
    if user_account == "quit":
        running = False
        break

    user_balance = float(input("Enter the balance: "))
    
    accounts.append(user_account)
    balances.append(user_balance)

    for i in range(len(accounts)):
        print(f"{i}. {accounts[i]} Balance: ${balances[i]:.2f}")



correct = input("Are the account and balance correct? (y/n): ")

if correct == "n":
    running_2 = True

while running_2:
        change = int(input("Which account number would you like to change? "))
        correct_balance = float(input(f"Enter the correct balance for {accounts[change]}: "))

        balances[change] = correct_balance

        more = input("Would you like to change another account? (y/n): ")
        if more == "n":
            running_2 = False
            break

print(f"The total balance is ${sum(balances:.2f)}")
print(f"The average balance is ${sum(balances) / len(balances)}")

highest_balance = max(balances)
highest_balance_index = balances.index(highest_balance)
print(f"The account with the highest balance is {accounts[highest_balance_index]} with ${highest_balance:.2f}")