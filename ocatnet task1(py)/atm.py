print("Welcome to ABC Bank!!")
import time

print("Insert your card")
time.sleep(3)
class ATM:
    def __init__(self, balance=2000):
        self.balance = balance
        self.transaction_history = []

    def display_balance(self):
        return f"Your balance is ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited ${amount}")
        return f"Deposited ${amount}. {self.display_balance()}"

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount}. {self.display_balance()}"

    def transfer(self, amount, recipient_user):
        if amount > self.balance:
            return "Insufficient funds for transfer"
        else:
            self.balance -= amount
            recipient_user.atm.deposit(amount)
            self.transaction_history.append(f"Transferred ${amount} to {recipient_user.name}")
            return f"Transferred ${amount} to {recipient_user.name}. {self.display_balance()}"

class User:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin
        self.atm = ATM()

def login():
    users = {"User1": "2620", "User2": "2003"}  # Replace with your user PINs
    while True:
        username = input("Enter username: ")
        if username in users:
            pin = input("Enter PIN: ")
            if pin == users[username]:
                return User(username, pin)
            else:
                print("Incorrect PIN. Please try again.")
        else:
            print("User not found. Please try again.")

def main():
    user = login()

    while True:
        print("1. Display Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            print(user.atm.display_balance())
        elif choice == "2":
            amount = float(input("Enter deposit amount: "))
            print(user.atm.deposit(amount))
        elif choice == "3":
            amount = float(input("Enter withdrawal amount: "))
            print(user.atm.withdraw(amount))
        elif choice == "4":
            amount = float(input("Enter transfer amount: "))
            user2 = login()
            print(user.atm.transfer(amount, user2))
        elif choice == "5":
            print("Transaction History:")
            for transaction in user.atm.transaction_history:
                print(transaction)
        elif choice == "6":
            print("Thank you . Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__== "__main__":
    main()