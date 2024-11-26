import time


def greeting():
    """Generates a greeting based on the time of day."""
    current_hour = time.localtime().tm_hour
    if current_hour < 12:
        return "Good Morning"
    elif current_hour < 18:
        return "Good Afternoon"
    else:
        return "Good Evening"


def validate_pin_input():
    """Ensures the user inputs a valid PIN."""
    try:
        pin = int(input("Enter your ATM PIN: "))
        if 1000 <= pin <= 9999:
            return pin
        else:
            print("Invalid PIN! It must be a 4-digit number.")
            return None
    except ValueError:
        print("Invalid input! Please enter a 4-digit PIN.")
        return None


def verify_pin(stored_pin):
    """Verify the user's PIN before performing an operation."""
    pin = validate_pin_input()
    if pin == stored_pin:
        return True
    print("Incorrect PIN!")
    return False


def check_balance(balance):
    """Display the user's current balance."""
    print(f"Your current balance is: ₹{balance}")


def withdraw_balance(balance, transaction_history):
    """Handle withdrawal of funds."""
    try:
        withdraw_amount = int(input("Enter the amount to withdraw: ₹"))
        if withdraw_amount > balance:
            print("Insufficient balance!")
        elif withdraw_amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance -= withdraw_amount
            print(f"₹{withdraw_amount} has been debited from your account.")
            print(f"Your updated balance is: ₹{balance}")
            transaction_history.append(f"Withdrawn: ₹{withdraw_amount}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    return balance


def deposit_balance(balance, transaction_history):
    """Handle deposit of funds."""
    try:
        deposit_amount = int(input("Enter the amount to deposit: ₹"))
        if deposit_amount <= 0:
            print("Amount must be greater than zero.")
        else:
            balance += deposit_amount
            print(f"₹{deposit_amount} has been credited to your account.")
            print(f"Your updated balance is: ₹{balance}")
            transaction_history.append(f"Deposited: ₹{deposit_amount}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    return balance


def view_transaction_history(transaction_history):
    """Display the transaction history."""
    print("Transaction History:")
    if transaction_history:
        for transaction in transaction_history:
            print(transaction)
    else:
        print("No transactions yet.")


def transfer_money(balance, transaction_history):
    """Handle money transfers."""
    try:
        transfer_amount = int(input("Enter the amount to transfer: ₹"))
        if transfer_amount <= 0:
            print("Transfer amount must be greater than zero.")
        elif transfer_amount > balance:
            print("Insufficient balance to complete the transfer.")
        else:
            recipient_account = input("Enter the recipient's account number: ")
            balance -= transfer_amount
            print(f"₹{transfer_amount} has been transferred to account {recipient_account}.")
            print(f"Your updated balance is: ₹{balance}")
            transaction_history.append(f"Transferred: ₹{transfer_amount} to {recipient_account}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")
    return balance


def change_pin(password):
    """Allow the user to change their PIN."""
    new_pin = input("Enter your new pin:")
    new_pin = validate_pin_input()
    if new_pin:
        password = new_pin
        print("Your PIN has been successfully changed.")
    return password


def main():
    print("Please insert your CARD")
    time.sleep(2)

    password = 1234
    balance = 5000
    attempts = 3
    transaction_history = []

    while attempts > 0:
        pin = validate_pin_input()
        if pin is None:
            continue

        if pin == password:
            print(f"{greeting()}! Welcome to Your Bank.")
            while True:
                print(
                    """
                Please choose an option:
                1. Check Balance
                2. Withdraw Balance
                3. Deposit Balance
                4. View Transaction History
                5. Transfer Money
                6. Change PIN
                7. Exit
                """
                )
                try:
                    option = int(input("Enter your choice: "))
                except ValueError:
                    print("Invalid input! Please select a valid option.")
                    continue

                if option in range(1, 7):  # Verify PIN for options 1 to 6
                    if not verify_pin(password):
                        continue

                if option == 1:
                    check_balance(balance)

                elif option == 2:
                    balance = withdraw_balance(balance, transaction_history)

                elif option == 3:
                    balance = deposit_balance(balance, transaction_history)

                elif option == 4:
                    view_transaction_history(transaction_history)

                elif option == 5:
                    balance = transfer_money(balance, transaction_history)

                elif option == 6:
                    password = change_pin(password)

                elif option == 7:
                    print("Thank you for using our ATM. Have a great day!")
                    break

                else:
                    print("Invalid option! Please choose a valid number.")

            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Wrong PIN! You have {attempts} attempts remaining.")
            else:
                print("Too many incorrect attempts. Your card has been blocked. Please contact customer support.")


if __name__ == "__main__":
    main()
