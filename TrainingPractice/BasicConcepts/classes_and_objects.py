

class BankAccount:
    """
    This class has methods to add money to account, withdraw money, calculate bak fess and display the account details.
    """
    def __init__(self, accountNum, name, balance=0):
        self.accountNum=accountNum
        self.name=name
        self.balance=balance
        
    def deposit(self, amount):
        self.balance += amount
        print(self.balance)
        
    def withdrawal(self, amount):
        self.balance -= amount
        print(self.balance)
        
    def bankFees(self):
        fees = 0.5*self.balance
        return fees
        
    def display(self):
        print(f'account number: {self.accountNum}, name: {self.name}, balance: {self.balance}')
        


class Rectangle:
    """
    This class has methods to calculate area of rectangle, perimeter and display the same.
    """
    def __init__(self, length, breadth):
        self.length=length
        self.breadth=breadth
      
    def area(self):
        return self.length*self.breadth
    
    def peri(self):
        return 2*(self.length+self.breadth)
    
    def display(self):
        print(f'length: {self.length} breadth: {self.breadth}, area: {self.area()}, perimeter: {self.peri()}')
        
class Parellelopiped(Rectangle):
    """
    This is child class inherited from parent class Rectangle.It calculates volume of rectangle.
    """
    def __init__(self, length, breadth, height):
        Rectangle.__init__(self, length, breadth)
        self.height=height
        
    def volume(self):
        return self.length*self.breadth*self.height
    