class Bank:
    def acc_create(self, name, age, branch, acc_type, balance):
        self.name = name
        self.age = age
        self.branch = branch
        self.acc_type = acc_type
        self.balance = balance
        print("Account created successfully! \nAccount details \n----------------")
        print("Name:", self.name, "\nAge:", self.age, "\nBranch:", self.branch, "\nAccount type:", self.acc_type,
              "\nAccount balance:", self.balance)

    def deposit(self, deposit_amount):
        self.deposit_amount = deposit_amount
        print(self.deposit_amount, "is successfully deposited")
        self.balance += self.deposit_amount
        print("New Balance:", self.balance)

    def withdraw(self, withdraw_amount):
        self.withdraw_amount = withdraw_amount
        if self.withdraw_amount > self.balance:
            print("Insufficient balance!")
        else:
            print(self.withdraw_amount, "is successfully withdrew")
            self.balance -= self.withdraw_amount
            print("Available balance :", self.balance)

    def balance_check(self):
        print("Available Balance:", self.balance)

    def exit(self):
        print("Thank you", self.name)


def bank():
    print("\nCreate account")
    b1 = Bank()
    ac_name = input("Enter the name: ")
    ac_age = int(input("Enter the age: "))
    ac_branch = input("Enter the branch: ")
    ac_acc_type = input("Enter the account type: ")
    ac_balance = int(input("Enter the initial balance: "))
    b1.acc_create(ac_name, ac_age, ac_branch, ac_acc_type, ac_balance)
    while True:
        print(" \n1. Deposit amount \n2. Withdraw amount \n3. Check balance \n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            acc_deposit = int(input("Enter the amount to deposit : "))
            b1.deposit(acc_deposit)
        elif choice == 2:
            acc_withdraw = int(input("Enter the amount to withdraw : "))
            b1.withdraw(acc_withdraw)
        elif choice == 3:
            b1.balance_check()
        elif choice == 4:
            b1.exit()
            break


bank()




