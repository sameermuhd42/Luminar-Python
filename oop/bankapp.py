class Bank:
    users = {
        1000: {"account_num": 1000, "password": "user1", "balance": 3000},
        1001: {"account_num": 1001, "password": "user2", "balance": 4000},
        1002: {"account_num": 1002, "password": "user2", "balance": 5000},
        1003: {"account_num": 1003, "password": "user3", "balance": 6000}
    }
    session = dict()

    def validate_account(self, acc_no):
        if acc_no in self.users:
            return True
        else:
            return False

    def authenticate(self, **kwargs):
        acc_no = kwargs.get("acc_num")
        password = kwargs.get("password")
        user = self.validate_account(acc_no)
        if user:
            if password == self.users[acc_no]["password"]:
                self.session["user"] = acc_no
                print("Login successfully")
                return acc_no
            else:
                print("Incorrect password")
                return -1
        else:
            print("Invalid account number")
            return 0

    def balance_enquiry(self, acc_no):
        if acc_no == self.session["user"]:
            print(self.users[acc_no]["balance"])
            # print(self.session)
        else:
            print("You must login to continue")

    def fund_transfer(self, user, to_acc_no, amount):
        if self.validate_account(to_acc_no):
            balance = self.users[user]["balance"]
            if balance < amount:
                print("Insufficient balance")
            else:
                self.users[user]["balance"] -= amount
                self.users[to_acc_no]["balance"] += amount

    def logout(self):
        self.session["user"] = 0
        print("Logout successfully")


obj = Bank()
user_login = obj.authenticate(acc_num=1000, password="user1")
if user_login == -1 or user_login == 0:
    print("Authentication failed")
else:
    obj.balance_enquiry(user_login)
obj.fund_transfer(user_login, 1001, 2000)
obj.balance_enquiry(user_login)
obj.logout()
