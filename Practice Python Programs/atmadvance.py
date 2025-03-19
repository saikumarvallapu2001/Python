print("Welcome to Kotak Mahindra Bank")

# List to store multiple users
users = [
    {'account_number': 645482, 'pin': 1919, 'balance': 5000, 'transactions': []},
    {'account_number': 123456, 'pin': 1234, 'balance': 3000, 'transactions': []}
]

# Function to find a user by account number and pin
def find_user(account_number, account_pin):
    for user in users:
        if user['account_number'] == account_number and user['pin'] == account_pin:
            return user
    return None

# Function to register a new user
def register_user():
    new_account_number = int(input("Enter a new Account Number: "))
    
    # Check if account number already exists
    for user in users:
        if user['account_number'] == new_account_number:
            print("Account Number already exists. Try again.")
            return
    
    new_pin = int(input("Enter a new PIN: "))
    initial_balance = float(input("Enter Initial Deposit Amount: "))

    # Add new user to the list
    users.append({
        'account_number': new_account_number,
        'pin': new_pin,
        'balance': initial_balance,
        'transactions': []
    })
    
    print("Account successfully created!")

# Main menu
while True:
    print("\n1. Login to ATM\n2. Register New Account\n3. Exit")
    main_choice = int(input("Enter your choice: "))

    if main_choice == 1:
        account_number = int(input("Enter Your ATM Account Number: "))
        account_pin = int(input("Enter Your ATM PIN: "))

        # Authenticate user
        user = find_user(account_number, account_pin)
        if not user:
            print("Invalid Account Number or PIN. Try again.")
        else:
            print("Login Successful!")

            while True:
                print("\nATM Menu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Logout")
                choice = int(input("Enter your choice: "))

                if choice == 1:
                    print("Current Balance: $", user['balance'])

                elif choice == 2:
                    deposit = float(input("Enter Deposit Amount: "))
                    user['balance'] += deposit
                    user['transactions'].append(f"Deposited: ${deposit}")
                    print("Deposit Successful! New Balance: $", user['balance'])

                elif choice == 3:
                    withdraw = float(input("Enter Withdrawal Amount: "))
                    if withdraw > user['balance']:
                        print("Insufficient Balance!")
                    else:
                        user['balance'] -= withdraw
                        user['transactions'].append(f"Withdrawn: ${withdraw}")
                        print("Withdrawal Successful! New Balance: $", user['balance'])

                elif choice == 4:
                    if not user['transactions']:
                        print("No Transactions Available.")
                    else:
                        print("Transaction History:")
                        for transaction in user['transactions']:
                            print(transaction)

                elif choice == 5:
                    print("Logging out...")
                    break

                else:
                    print("Invalid Input. Please Try Again.")

    elif main_choice == 2:
        register_user()  # Call function to register new users

    elif main_choice == 3:
        print("Thank you for using Kotak Mahindra Bank ATM. Goodbye!")
        break

    else:
        print("Invalid Choice! Please try again.")
