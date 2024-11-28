import time

print("Please insert Your CARD")
# card processing
time.sleep(3)
password = 5462
# taking atm pin from user
pin = int(input("Enter your ATM PIN: "))
balance = 11000
transaction_history = []  # List to store transaction history

# checking if pin is valid or not
if pin == password:
    while True:
        # Showing info to user
        print("""
            1 == Check Balance
            2 == Withdraw Balance
            3 == Deposit Balance
            4 == Transaction History
            5 == Change PIN
            6 == Exit
        """)

        try:    
            # taking an option from user
            option = int(input("Please enter your choice: "))
        except ValueError:
            print("Please enter a valid option")
            continue  # skip to the next iteration if input is invalid

        # for option 1        
        if option == 1:
            print(f"Your current balance is {balance}")

        elif option == 2:
            withdraw_amount = int(input("Please enter withdraw amount: "))
            if withdraw_amount > balance:
                print("Insufficient funds")
            else:
                balance -= withdraw_amount
                print(f"{withdraw_amount} is debited from your account")
                print(f"Your updated balance is {balance}")
                transaction_history.append(f"Withdrew: {withdraw_amount} | Balance: {balance}")

        elif option == 3:
            deposit_amount = int(input("Please enter deposit amount: "))
            balance += deposit_amount
            print(f"{deposit_amount} is credited to your account")
            print(f"Your updated balance is {balance}")
            transaction_history.append(f"Deposited: {deposit_amount} | Balance: {balance}")

        elif option == 4:
            if transaction_history:
                print("Transaction History:")
                for transaction in transaction_history:
                    print(transaction)
            else:
                print("No transactions yet.")
        
        elif option == 5:
            # Change PIN option
            current_pin = int(input("Enter your current PIN: "))
            if current_pin == password:
                new_pin = int(input("Enter your new PIN: "))
                confirm_new_pin = int(input("Confirm your new PIN: "))
                if new_pin == confirm_new_pin:
                    password = new_pin
                    print("PIN successfully changed!")
                else:
                    print("PINs do not match. Please try again.")
            else:
                print("Incorrect current PIN.")

        elif option == 6:
            print("Thank you for using our service!")
            break
        else:
            print("Invalid option, please try again.")
else:
    print("Wrong PIN. Please try again")