

# class Account:
#     def __init__(self,number,pin):
#         self.number = number
#         self.__pin = pin
#         self.__balance = 500

#     def show_balance(self,pin):
#         if pin == self.__pin:
#             return self.__balance
#         else:
#             return "wrong pin"
        
# acc  = Account(number=1234,pin=5678)

# print(acc.show_balance(8765))
# print(acc.show_balance(5678))


class Account:
    def __init__(self,name,accountNumber):
        self.name = name
        self.balance = 0
        self.accountNumber = accountNumber
        self.history = []
        self.id = 0
        self.loan = 0


    def display_details(self):
        print(f"Name: {self.name} \n account no.: {self.accountNumber}")

    def change_account_details(self,name,accountNUmber):
        self.name = name
        self.accountNumber = accountNUmber

    def deposit(self,amount):

        from datetime import date

        time = date.today()

        transaction_time = time.strftime("%Y-%m-%d")

        self.balance += amount
        print(f"Hello {self.name} you have deposited {amount}KESH successfully! Current balance: {self.balance}KESH")
        self.id +=1

        record = {"id":self.id,"Amount":amount,"transaction_type":"Deposit","Date":transaction_time}
        self.history.append(record)

        # print(f"History:\n {self.history}")

    def withdraw(self,amount):

        from datetime import date

        time = date.today()

        transaction_time = time.strftime("%Y-%m-%d")

        if amount < self.balance:

           self.balance -= amount
           print(f"Hello {self.name}, {amount}KESH has been withdrawn from your account successfully! Current balance: {self.balance}KESH")
           self.id +=1

           record = {"id":self.id,"Amount":amount,"transaction_type":"Withdraw","Date":transaction_time}
           self.history.append(record)

        else: print(f"Hello {self.name}, your balance is insuffient\n You can ask for an overdraft")

        # print(f"History:\n {self.history}")

    def account_statement(self):
        print(f"Hello {self.name} with Account no. {self.accountNumber} your current balance is {self.balance}KESH")


    def overdraft_limit(self,loan_amount):

        from datetime import date

        time = date.today()

        transaction_time = time.strftime("%Y-%m-%d")


        if loan_amount <= (self.balance + (3000 - self.loan)):
            self.loan += (loan_amount - self.balance)
            self.balance = 0
            print(f"Hello {self.name} Your account balance: {self.balance} with loan:{self.loan}")
            self.id +=1

            record = {"id":self.id,"Amount":loan_amount,"transaction_type":"Withdraw & loan","Date":transaction_time}
            self.history.append(record)
           

        else:
             print(f"You have exceeded Overdraft")

    
    def transaction_history(self):
        print(f"Transaction History: \n {self.history}")