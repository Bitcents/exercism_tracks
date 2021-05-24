from __future__ import division, annotations

def get_gcd(a: int, b: int) -> int:
        if a < b:
            a, b = b,a
    
        r = a%b
        while r != 0:
            a = b
            b = r
            r = a%b
        return b


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.reduce_to_lowest()

    def __eq__(self, other) -> bool:
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other) -> Rational:
        numer = self.numer * other.denom + other.numer*self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other) -> Rational:
        numer = self.numer * other.denom - other.numer*self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other) -> Rational:
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __truediv__(self, other) -> Rational:
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        return Rational(numer, denom)

    def __abs__(self) -> Rational:
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power) -> Rational:
        if power >= 0:
            return Rational(pow(self.numer, power), pow(self.denom, power))
        else:
            return Rational(pow(self.numer, abs(power)), pow(self.numer, abs(power)))

    def __rpow__(self, base) -> float:
        power: float = self.numer / self.denom
        return base ** power
    
    def reduce_to_lowest(self) -> None:
        if self.numer == 0:
            self.denom = 1
        else:
            gcd = get_gcd(self.denom, self.numer)
            self.denom = self.denom // gcd
            self.numer = self.numer // gcd

        if self.denom < 0:
            self.numer *= -1
            self.denom *= -1



a = Rational(2, -5)
print(a)