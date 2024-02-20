import math
 
class Complex:
    """
    Represents a complex number with real and imaginary parts.
    """
 
    def __init__(self, re=0, im=0):
        """
        Initialize a complex number with real and imaginary parts.
 
        Args:
        - re (int or float): Real part of the complex number.
        - im (int or float): Imaginary part of the complex number.
        """
        self.re = re
        self.im = im
 
    def __add__(self, other):
        """
        Add two complex numbers or add a real/imaginary number to a complex number.
 
        Args:
        - other (int, float, Complex): Another complex number or a real/imaginary number.
 
        Returns:
        - Complex: Result of the addition.
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re + other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else:
            raise TypeError("Unsupported operand type for addition")
 
    def __sub__(self, other):
        """
        Subtract two complex numbers or subtract a real/imaginary number from a complex number.
 
        Args:
        - other (int, float, Complex): Another complex number or a real/imaginary number.
 
        Returns:
        - Complex: Result of the subtraction.
        """
        if isinstance(other, int) or isinstance(other, float):
            return Complex(self.re - other, self.im)
        elif isinstance(other, Complex):
            return Complex(self.re - other.re, self.im - other.im)
        else:
            raise TypeError("Unsupported operand type for subtraction")

    
    def __mul__(self, other):

        if isinstance(other, int) or isinstance(other, float):

            return Complex(self.re * other, self.im * other)

        elif isinstance(other, Complex):

        #   (a+bi)*(c+di) = ac + adi +bic -bd
            a = self.re
            b = self.im
            c = other.re
            d = other.im

            return Complex(a * c - b * d, 

                           a * d + b * c)

        else:
            raise TypeError
    
    def __truediv__(self, other):

        if isinstance(other, int) or isinstance(other, float):

            return Complex(self.re / other, self.im / other)

        elif isinstance(other, Complex):
            a = self.re
            b = self.im
            c = other.re
            d = other.im

            repart = 1/(c**2+d**2)*(a*c + b*d)

            impart = 1/(c**2+d**2)*(b*c - a*d)

            return Complex(repart,impart)

        else:
            raise TypeError
        
    
    def __str__(self):
        if self.im>=0:
            return '%.2f + %.2fi'% (self.re, self.im)
        else:
            return "%.2f%.2fi" % (self.re, self.im)
        
    def __repr__(self):
        return self.__str__()
