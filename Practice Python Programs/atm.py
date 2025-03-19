print('Welcome to Kotak Mahindra Bank')

account_number = int(input("Enter Your ATM Account Number: "))
account_pin = int(input("Enter Your ATM Pin: "))

user_details = {
    'user_account_number': 645482,
    'user_pin': 1919,
    'balance': 5000,
    'transaction': []
}

if user_details["user_account_number"] != account_number or user_details['user_pin'] != account_pin:
    print("Invalid Account Number or PIN")
else:
    print("Login Successful")

    while True:
        print("\nATM Menu:\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance: $", user_details['balance'])

        elif choice == 2:
            deposit = int(input("Enter Deposit Amount: "))
            user_details['balance'] += deposit
            user_details['transaction'].append(f"Deposited: {deposit}")
            print("Deposit Successful! New Balance: ", user_details['balance'])

        elif choice == 3:
            withdraw = int(input("Enter Withdrawal Amount: "))
            if withdraw > user_details['balance']:
                print("Insufficient Balance!")
            else:
                user_details['balance'] -= withdraw
                user_details['transaction'].append(f"Withdrawn: ${withdraw}")
                print("Withdrawal Successful! New Balance: $", user_details['balance'])

        elif choice == 4:
            if not user_details['transaction']:
                print("No Transactions Available.")
            else:
                print("Transaction History:")
                for transaction in user_details['transaction']:
                    print(transaction)

        elif choice == 5:
            print("Thank You for Visiting Kotak Mahindra Bank!")
            break

        else:
            print("Invalid Input. Please Try Again.")
