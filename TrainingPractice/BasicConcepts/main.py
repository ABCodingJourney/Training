import logging
from classes_and_objects import BankAccount, Rectangle, Parellelopiped
from decorators import my_func
from dunder_methods_1 import Account
from dunder_methods_2 import Complex
from loggingConfigs import logConfig

logConfig()

def class_and_objs():
    try:
        #creating object of class BankAccount   
        account = BankAccount(123, "ananya", 1000)
        account.display()
        #adding 500rs
        account.deposit(500)
        #withdrawing 200rs
        account.withdrawal(200)
        
        rec = Rectangle(2,4)
        rec.display()

        pp = Parellelopiped(2,4,4)
        logging.info(pp.volume())
        
    except Exception as e:
        logging.exception(f"Error Occurred: {e}")
        


def decorator_fun():
    try:
        logging.info("Executing decorator function")
        my_func()    
        
    except Exception as e:
        logging.exception(f"Error Occurred: {e}")
        
    else:
        logging.info("Done")


def dunder_methods():
    try:
        
        logging.info("Dunder examples for __add__")
        acc1 = Account("AccNum1", 1000)
        acc2 = Account("AccNum2", 2000)

        logging.info(acc1+acc2) #can add two objects of account class

        # acc1+3 #cant add anything else to acc object - throws error

        logging.info("Dunder methods example for __add__, __sub__, __mul__, __trudiv__, __str__, __repr__")
        x = Complex(3, 2)
        y = Complex(4, 5)

        logging.info(x+y)   #calls internally __str__
        logging.info(x-y)
        logging.info(x*y)
        logging.info(x/y)

        x+y   #calls internally __repr__
        
    except Exception as e:
        logging.exception(f"Error Occurred: {e}")
        

if __name__ == '__main__':
     
    class_and_objs()
    decorator_fun()
    dunder_methods()
