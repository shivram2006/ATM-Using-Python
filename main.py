
class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin

class Transaction:
    def __init__(self, amount):
        self.amount = amount

class Withdrawal(Transaction):
    def __init__(self, amount):
        super().__init__(amount)

class Deposit(Transaction):
    def __init__(self, amount):
        super().__init__(amount)

class ATM:
    def __init__(self):
        self.users = {}
        self.transactions = []

    def add_user(self, user):
        self.users[user.user_id] = user

    def authenticate_user(self, user_id, pin):
        if user_id in self.users and self.users[user_id].pin == pin:
            return True
        else:
            return False

    def transaction_history(self):
        for transaction in self.transactions:
            print(transaction.amount)

    def withdraw(self, amount):
        self.transactions.append(Withdrawal(amount))

    def deposit(self, amount):
        self.transactions.append(Deposit(amount))

    def transfer(self, amount, recipient_id):
        if recipient_id in self.users:
            self.transactions.append(Withdrawal(amount))
            self.users[recipient_id].deposit(amount)
        else:
            print("Recipient not found.")

# Main function
def main():
    atm = ATM()

    # Creating some users
    user1 = User("123456", "1234")
    user2 = User("789012", "5678")

    # Adding users to the ATM
    atm.add_user(user1)
    atm.add_user(user2)

    # User authentication
    user_id = input("Enter user ID: ")
    pin = input("Enter PIN: ")

    if atm.authenticate_user(user_id, pin):
        print("Authentication successful.")
        while True:
            print("Choose operation:")
            print("1. Transaction History")
            print("2. Withdraw")
            print("3. Deposit")
            print("4. Transfer")
            print("5. Quit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("Transaction History:")
                atm.transaction_history()
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                atm.withdraw(amount)
                print("Withdrawal successful.")
            elif choice == "3":
                amount = float(input("Enter deposit amount: "))
                atm.deposit(amount)
                print("Deposit successful.")
            elif choice == "4":
                amount = float(input("Enter transfer amount: "))
                recipient_id = input("Enter recipient's user ID: ")
                atm.transfer(amount, recipient_id)
                print("Transfer successful.")
            elif choice == "5":
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    else:
        print("Authentication failed. Invalid user ID or PIN.")

if __name__ == "__main__":
    main()
