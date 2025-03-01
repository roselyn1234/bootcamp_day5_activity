balance = 10
interest_rate = 0.05  # 5% interest rate

while True:
    print("\n1. Deposit  2. Withdraw  3. Balance  4. Apply Interest  5. Exit")
    choice = input("Choose: ")

    if choice == '1':
        deposit_amount = float(input("Deposit amount: "))
        balance += deposit_amount
        print(f"${deposit_amount} deposited successfully.")
    elif choice == '2':
        withdraw_amount = float(input("Withdraw amount: "))
        if withdraw_amount > balance:
            print("Insufficient funds.")
        else:
            balance -= withdraw_amount
            print(f"${withdraw_amount} withdrawn successfully.")
    elif choice == '3':
        print(f"Balance: ${balance}")
    elif choice == '4':
        interest = balance * interest_rate
        balance += interest
        print(f"Interest of ${interest} applied. New balance: ${balance}")
    elif choice == '5':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")