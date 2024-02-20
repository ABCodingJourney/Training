import time

def log_time(func):
    ''' Log the time taken to execute function'''
    
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        print(f'{func.__name__} ran in {t2} seconds')
        
    return wrapper

@log_time
def my_func():
    print("Hi hello")
    x = 5
    y = 6
    print(x+y)
