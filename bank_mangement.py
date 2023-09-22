class Bank:
    initial_bank_balance = 0
    total_loan_amount = 0
    loan_feature_enabled = True

    @staticmethod
    def get_bank_balance():
        return Bank.initial_bank_balance

    @staticmethod
    def get_total_loan_amount():
        return Bank.get_total_loan_amount

class User:
    def __init__(self, user_name, user_account_number, user_balance=0):
        self.user_name = user_name
        self.user_account_number = user_account_number
        self.user_balance = user_balance
        self.user_transaction_history = []

    def deposit(self, amount):
        self.user_balance += amount
        Bank.initial_bank_balance += amount
        self.user_transaction_history.append(f'Deposited amount: {amount}')

    def withdraw(self, amount):
        if self.user_balance >= amount:
            self.user_balance -= amount
            Bank.initial_bank_balance -= amount
            self.user_transaction_history.append(f'Withdrew amount: {amount}')
        else:
            print("Sorry, your account does not have enough funds for this transaction")

    def transfer(self, recipient, amount):
        if self.user_balance >= amount:
            self.user_balance -= amount
            recipient.initial_bank_balance += amount
            self.user_transaction_history.append(
                f'Transferred {amount} to account {recipient.user_account_number}')
            recipient.user_transaction_history.append(
                f'Received {amount} from account {self.user_account_number}')
        else:
            print("Does not have enough funds!")

    def check_balance(self):
        return self.user_balance

    def take_loan(self):
        if Bank.loan_feature_enabled:
            loan_limit = self.user_balance * 2
            if Bank.total_loan_amount < loan_limit:
                self.user_balance += self.user_balance
                Bank.initial_bank_balance += self.user_balance
                self.user_transaction_history.append(
                    f'Took a loan of amount: {self.user_balance}')
                Bank.total_loan_amount += self.user_balance
            else:
                print("You have reached the maximum loan amount allowed!")
        else:
            print("Sorry, you can't take a loan right now. Please try again later.")

    def check_transaction_history(self):
        return self.user_transaction_history

class Admin:
    def create_user_account(self, name, account_number, initial_deposit=0):
        return User(name, account_number, initial_deposit)

    @staticmethod
    def check_bank_balance():
        return Bank.check_bank_balance()

    @staticmethod
    def check_total_loan_amount():
        return Bank.check_total_loan_amount()

    @staticmethod
    def loan_feature_on():
        Bank.loan_feature_enabled = True
        print("Loan feature is now available!")

    @staticmethod
    def loan_feature_off():
        Bank.loan_feature_enabled = False
        print("You can now borrow money.")

admin = Admin()

print('====== User Information  ========')

user1 = admin.create_user_account("Mithila", 202031058004, initial_deposit=20000)
user2 = admin.create_user_account("Shakib Al Hasan", 202031058075, initial_deposit=21000)
print(user1.user_name, user1.user_account_number, user1.user_balance)
print(user2.user_name, user2.user_account_number, user2.user_balance)

print('======After Deposite========')
user1.deposit(5000)
user2.deposit(9000)
print('User 1 balanace :' , user1.check_balance())
print('User 2 balanace :' , user2.check_balance())







