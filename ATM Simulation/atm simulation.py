print("Welcome To ATM")
#Actual Account Detials
real_account_number = 240128010004
real_pin = 5458
#Balance
Balance = 30000
#User input 
user_account_number = int(input("Enter the account number: "))
user_pin = int(input("Enter the Pin: "))

if user_account_number == real_account_number and user_pin == real_pin:
    print("Login Successful!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")
    
        choose = int(input("Enter the choice: "))
        if choose == 1:
            print("Check Balance")
            print("Balance:",Balance)
        elif choose == 2:
            print("Deposit")
            Deposit = int(input("Enter the deposit amount: "))
            if Deposit > 0:
                Balance += Deposit
                print("Update Balance:",Balance)
            else:
                print("Please enter a valid amount.")
        elif choose == 3:
            print("Withdraw")
            Withdraw = int(input("Enter the withdraw amount: "))
            if Balance >= Withdraw and Withdraw > 0:
                Balance -= Withdraw  
                print("Update Balance:",Balance)
            elif Withdraw <= 0:
                print("Please enter a valid amount. ")
            else:
                print("Insufficient Balance.")
        elif choose == 4:
            print("Change PIN")
            current_pin = int(input("Enter the current pin: "))
            if current_pin == real_pin:
                new_pin = int(input("Enter the new pin: "))
                confirm_pin = int(input("Enter the confirm pin: "))
                if  new_pin == confirm_pin:
                    real_pin = new_pin
                    print("PIN updated successfully.")
                else:
                    print("New PIN and Confirm PIN do not match.")
            else:
                print("Current PIN is incorrect.")
        elif choose == 5:
            print("Thank you for using our ATM. Have a nice day!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Invalid account number or pin ")