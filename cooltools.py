__author__  = "smiks"
__version__ = "0.2"

from math import sqrt
from itertools import permutations

class cooltools:

    def __init__(self):
        self.firstHundredPrimes = self.primesC(100)         # little cache
        self.firstFiveHundredPrimes = self.primesC(500)     # little cache
        self.firstThousandPrimes = self.primesC(1000)       # little cache

    # sieve of eratosthenes :: returns dictionary with key:value where key is number
    # and value is boolean - true if prime false if not
    def esieve(self, num):
        primes = { i:(not(i == 2 or i % 2 == 0 or i == 0 or i == 1)) for i in range(num+1) }
        primes[2] = True
        limit   = sqrt(num) + 1
        i       = 3
        while i <= limit:
            if primes[i]:
                j = 2 * i
                while j < num:
                    primes[j] = False
                    j += i
            i += 2
        return primes

    # cache function :: used for cache variables in __init__
    def primesC(self, num):
        return [i for i,j in self.esieve(num).items() if j ]

    # function generates list of primes
    def primes(self, num):
        if num == 100:
            return self.firstHundredPrimes
        if num == 500:
            return self.firstFiveHundredPrimes
        if num == 1000:
            return self.firstThousandPrimes
        return [i for i,j in self.esieve(num).items() if j ]

    # generator generating prime numbers
    def primesGenerator(self, num):
        return ( i for i,j in self.esieve(num).items() if j )

    def isPrime(self, n):
        if n < 2:
            return False

        # taking care of first 10 integers
        if n == 4 or n == 6 or n == 8 or n == 9 or n == 10:
            return False
        if n == 2 or n == 3 or n == 5 or n == 7 or n == 11:
            return True

        # taking care of multipliers (of first 10 integers)
        if n > 11 and (n%2 == 0 or n%3 == 0 or n%5 == 0 or n%7 == 0 or n%11 == 0):
            return False

        # using cache to check first thousand primes
        if n in self.firstThousandPrimes:
            return True

        #checking the rest
        for i in range(5, int(sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    # function returns primefactors of number a
    def primefactors(self, a):
        factors = list()
        if sqrt(a) > 1000:
            primelist = self.primes((a // 2) + 1)
        else:
            primelist = self.firstThousandPrimes
        for i in primelist:
            while a%i == 0:
                a = a // i
                factors.append(i)
            if a == 1:
                break
        return factors

    # generator generating fibonacci numbers
    def fibonacciGenerator(self, n):
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

    # returns tuple containing min and max value from the list
    def findMinMax(self, list):
        tmin = list[0]
        tmax = list[0]
        for i,j in zip(list[0::2], list[1::2]):
            if i < j:
                tmin = min(tmin, i)
                tmax = max(tmax, j)
            else:
                tmin = min(tmin, j)
                tmax = max(tmax, i)
        return (tmin, tmax)

    # generator for pandigital numbers
    # receives list which contains digits
    def pandigitalsGenerator(self, lst):
        for i in permutations(lst):
            yield int(''.join(map(str,i)))

    # def isPandigital(a)