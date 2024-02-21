from exception_handling_eg1 import example
from exception_handling_eg2 import openFile


if __name__ == '__main__':
    
    #Execute example 1
    example()

    #Open a file and catch the errors
    openFile('corrupt_file.txt')