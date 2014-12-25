__author__  = "smiks"
__version__ = "0.3.1"

from math import sqrt
from itertools import permutations
from collections import defaultdict

class cooltools:

    def __init__(self):
        self.firstHundredPrimes = self.primesC(100)         # little cache
        self.firstFiveHundredPrimes = self.primesC(500)     # little cache
        self.firstThousandPrimes = self.primesC(1000)       # little cache

    # sieve of eratosthenes :: returns dictionary with key:value where key is number
    # and value is boolean - true if prime false if not
    def ESieve(self, n):
        primes = { i:(not(i == 2 or i % 2 == 0 or i == 0 or i == 1)) for i in range(n+1) }
        primes[2] = True
        limit   = sqrt(n) + 1
        i       = 3
        while i <= limit:
            if primes[i]:
                j = 2 * i
                while j < n:
                    primes[j] = False
                    j += i
            i += 2
        return primes

    # cache function :: used for cache variables in __init__
    def primesC(self, n):
        return {i for i,j in self.ESieve(n).items() if j }

    # function generates list of primes
    def primes(self, n):
        if n == 100:
            return self.firstHundredPrimes
        if n == 500:
            return self.firstFiveHundredPrimes
        if n == 1000:
            return self.firstThousandPrimes
        return [i for i,j in self.ESieve(n).items() if j ]

    # generator generating prime numbers
    def primesGenerator(self, n):
        return ( i for i,j in self.ESieve(n).items() if j )

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
    def primeFactors(self, a):
        factors = list()
        if self.isPrime(a):
            return [a]
        if (a // 2) > 1000:
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

    # function checks if given number is pandigital
    # lst accepts list or set which is used as rule.
    # Eg. isPandigital(n, {1,2,3}) it will check if n is pandigital number with digits 1, 2 and 3
    def isPandigital(self, num, lst):
        if len(str(num)) != len(lst):
            return False
        d = defaultdict(int)
        for i in str(num):
            i = int(i)
            if i not in lst:
                return False
            d[i] += 1
            if d[i] > 1:
                return False
        return True