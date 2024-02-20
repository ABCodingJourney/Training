#lets look at defining __add__ dunder method to custom class account

class Account:
    def __init__(self, accountName, balance=0):
        self.accountName = accountName
        self.balance = balance
        
    def __add__(self, accObj):
        if isinstance(accObj, Account):
            return self.balance+accObj.balance
        
        raise Exception(f"{accObj} is not of class Account")
