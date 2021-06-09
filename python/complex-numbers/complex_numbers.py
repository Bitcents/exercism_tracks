class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return self.real == other.real and self.imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self.real*other.real - self.imaginary*other.imaginary, self.real*other.imaginary + self.imaginary*other.real)

    def __sub__(self, other):
        return ComplexNumber(self.real - other.real, self.imaginary - other.imaginary)

    def __truediv__(self, other):
        numerator = self * other.conjugate()
        denominator = other.real**2 + other.imaginary**2
        return ComplexNumber(numerator.real/denominator, numerator.imaginary/denominator)

    def __abs__(self):
        from math import sqrt
        return sqrt(self.real**2 + self.imaginary**2)

    def conjugate(self):
        return ComplexNumber(self.real, -1*self.imaginary)

    def exp(self):
        from math import e, sin, cos
        return ComplexNumber(cos(self.imaginary)*pow(e, self.real), sin(self.imaginary)*pow(e, self.real))
