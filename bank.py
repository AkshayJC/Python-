import random

class Bank:
    def __init__(self, name, accType):
        self.name = name
        self.accNo = random.randint(1111111, 9999999)
        self.balance = 0
        self.accType = accType
        self.isCreated = True

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposit Successful! New Balance: {self.balance}\n")

    def withdraw(self):
        if self.balance <= 0:
            print("No funds available for withdrawal.\n")
            return
        withdrawAmount = int(input("Enter amount to withdraw: "))
        if withdrawAmount <= 0:
            print("Withdrawal amount must be positive.\n")
        elif self.balance >= withdrawAmount:
            self.balance -= withdrawAmount
            print(f"Withdrawal Successful! Remaining Balance: {self.balance}\n")
        else:
            print("Insufficient balance.\n")

    def check_balance(self):
        print(f"Account Number: {self.accNo}")
        print(f"Current Balance: {self.balance}\n")

def main():
    name = input("Enter account holder name: ")
    accType = input("Enter account type (Saving/Current): ")
    bank = Bank(name, accType)
    
    while True:
        print("\n====== BANK MENU ======")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("=======================")
        choice = input("Enter your choice (1-4): ")
        
        match choice:
            case "1":
                bank.deposit()
            case "2":
                bank.withdraw()
            case "3":
                bank.check_balance()
            case "4":
                print("Thank you for banking with us!")
                break
            case _:
                print("Invalid choice! Please select between 1-4.\n")

if __name__ == "__main__":
    main()