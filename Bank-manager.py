class Account:
    def get_input(self):
        self.balance = 220000
        print(f"Avaiable balance is {self.balance} ")
        self.account_no = int(input("Account number  : \n"))

    def credit(self):
        self.credited_amount = int(input("How much amount you want to credit ?\n"))
        self.total = self.balance + self.credited_amount
        return self.total
     
    def debit(self):
        self.debited_amount = int(input("Enter amount you want to debit\n"))

        if self.debited_amount > self.total:
            exit("Invalid Request")
        else:    
             self.debitedamount = self.total - self.debited_amount
             return self.debitedamount
        
        

a1 = Account()
a1.get_input(),a1.credit()

print(f"Account Number {a1.account_no} with balance {a1.balance} $\n")
print(f"New credited amount is {a1.total} $")
   
a1.debit()
print(f"Debited amount is {a1.debitedamount}")

    


 



