import math
from colors import bcolors

class TrapezoidalRule:
    def __init__(self, f, a, b, n):
        self.f = f
        self.a = a
        self.b = b
        self.n = n

    def integrate(self):
        h = (self.b - self.a) / self.n
        T = self.f(self.a) + self.f(self.b)
        integral = 0.5 * T  # Initialize with endpoints

        for i in range(1, self.n):
            x_i = self.a + i * h
            integral += self.f(x_i)

        integral *= h

        return integral

if __name__ == '__main__':
    f = lambda x: math.e ** (x ** 2)
    trapezoidal = TrapezoidalRule(f, 0, 1, 2)
    result = trapezoidal.integrate()
    print(bcolors.OKBLUE, "Approximate integral:", result, bcolors.ENDC)
