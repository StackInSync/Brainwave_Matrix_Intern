class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: $"))
            if amount <= 0:
                print("Deposit amount must be greater than zero.")
            else:
                self.balance += amount
                print(f"${amount:.2f} deposited successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: $"))
            if amount <= 0:
                print("Withdrawal amount must be greater than zero.")
            elif amount > self.balance:
                print("Insufficient balance.")
            else:
                self.balance -= amount
                print(f"${amount:.2f} withdrawn successfully.")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")


def verify_pin():
    try:
        with open("pin.txt", "r") as file:
            stored_pin = file.read().strip()
    except FileNotFoundError:
        print("PIN file not found.")
        return False

    entered_pin = input(f"Enter your {len(stored_pin)}-digit PIN: ").strip()

    if len(entered_pin) != len(stored_pin):
        print(f"PIN must be exactly {len(stored_pin)} digits.")
        return False

    if entered_pin == stored_pin:
        return True
    else:
        print("Incorrect PIN.")
        return False


# ---------- Main program loop ----------

def main():
    account = BankAccount()

    while True:
        print("\n--- Bank Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice in ['1', '2', '3']:
            if verify_pin():
                if choice == '1':
                    account.deposit()
                elif choice == '2':
                    account.withdraw()
                elif choice == '3':
                    account.check_balance()
            # If PIN is incorrect, the function won't be called.
        elif choice == '4':
            print("Thank you for using our bank system.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
