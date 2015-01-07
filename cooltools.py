__author__  = "smiks"
__version__ = "0.6"

from math import sqrt
from itertools import permutations
from collections import defaultdict
from functools import reduce
from collections import Counter

class cooltools:

    def __init__(self):
        self.firstThousandPrimes = self.primesC(8000)       # little cache ( generates first 1007 prime numbers)

    # sieve of eratosthenes :: returns dictionary with key:value where key is number
    # and value is boolean - true if prime false if not
    def ESieve(self, n):
        try:
            int(n)
        except ValueError:
            return {}
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
        try:
            int(n)
        except ValueError:
            return []
        return [i for i,j in self.ESieve(n).items() if j ]


    def firstNPrimes(self, n):
        try:
            int(n)
        except ValueError:
            return []
        if n < 0:
            return [];
        if n <= 1000:
            return self.firstThousandPrimes[:n]
        primes  = self.firstThousandPrimes[:1000]
        i       = primes[999]
        counter = 1000
        while True:
            if counter == n:
                return primes
            if self.isPrime(i):
                primes.append(i)
                counter += 1
            i += 1
        return primes


    # function generates list of primes below n
    def primes(self, n):
        try:
            int(n)
        except ValueError:
            return []
        if n < 0:
            return [];
        # if n < 7000 definitely in firstThousandPrimes list
        if n <= 7000:
            return [i for i in self.firstThousandPrimes if i < n]
        return [i for i,j in self.ESieve(n).items() if j ]

    # generator generating prime numbers
    def primesGenerator(self, n):
        try:
            int(n)
        except ValueError:
            return []
        return ( i for i,j in self.ESieve(n).items() if j )

    # used for internal functions
    def xprimesGenerator(self):
        counter = 1
        while True:
            if self.isPrime(counter):
                yield counter
            counter += 1


    def isPrime(self, n):
        try:
            int(n)
        except ValueError:
            return -1

        # if less than 2 - not a prime
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
        start = self.firstThousandPrimes[len(self.firstThousandPrimes)-1]
        for i in range(start, int(sqrt(n)) + 1, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False
        return True

    # function returns primefactors of number a
    def primeFactors(self, n):
        try:
            int(n)
        except ValueError:
            return []
        factors = list()
        if self.isPrime(n):
            return [n]
        if (n // 2) > 1000:
            primelist = self.primes((n // 2) + 1)
        else:
            primelist = self.firstThousandPrimes
        for i in primelist:
            while n%i == 0:
                n = n // i
                factors.append(i)
            if n == 1:
                break
        return factors

    # returns number of divisors
    def numDivisors(self, n):
        if n < 1:
            return 0
        if n == 1:
            return 1
        divs = Counter(self.primeFactors(n)).items()
        return reduce(lambda x,y: x*y, [i+1 for _,i in divs])

    # generator generating fibonacci numbers
    def fibonacciGenerator(self, n):
        try:
            int(n)
        except ValueError:
            return False
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

    # returns tuple containing min and max value from the list
    def findMinMax(self, list):
        tmin = list[0]
        tmax = list[0]
        if len(list)%2 != 0:
            list.append(list[0])
        for i,j in zip(list[0::2], list[1::2]):
            try:
                int(i)
                int(j)
            except ValueError:
                return False
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
        for i in lst:
            try:
                int(i)
            except ValueError:
                return []
        if any(i < 0 for i in lst):
            return -1
        for i in permutations(lst):
            yield int(''.join(map(str,i)))

    # function checks if given number is pandigital
    # lst accepts list or set which is used as rule.
    # Eg. isPandigital(n, {1,2,3}) it will check if n is pandigital number with digits 1, 2 and 3
    def isPandigital(self, n, lst):
        for i in lst:
            try:
                int(n)
            except ValueError:
                return False
        if n < 1:
            return False
        if len(str(n)) != len(lst):
            return False
        d = defaultdict(int)
        for i in str(n):
            i = int(i)
            if i not in lst:
                return False
            d[i] += 1
            if d[i] > 1:
                return False
        return True
