import logging

def logConfig():
    logging.basicConfig(
        level=logging.INFO,
        filename='employee_logs.log',
        format='%(asctime)s %(levelname)s %(message)s',
        datefmt="%d-%m-%Y %H:%M:%S"
    )

logConfig()

class Employee:
    def __init__(self, first, last):
        self.first=first
        self.last=last
        logging.info(f"Created employee {self.fullname()}")

    def displayDetails(self):
        if isinstance(self, Employee):
            logging.info(f"Employee's firstname is {self.first} and last name is {self.last}")
        
        else:
            logging.error("Object is not of Employee class")
        

    def fullname(self):
        return f"{self.first} {self.last}"


if __name__ == "__main__":
    
    emp1 = Employee("ananya", "bhat")
    emp2 = Employee("ananya", "b")
    emp1.displayDetails()
    

