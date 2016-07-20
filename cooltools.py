from math import factorial, sqrt
from itertools import chain, permutations, product
from collections import Counter, defaultdict
from functools import reduce
from heapq import heapify, heappop

"""
Cooltools module has bunch of useful functions.
Module can be used for work with prime numbers, fibonacci sequence,
some basic operations on lists and pandigital numbers.
Compatible for python versions Python 3.3 and Python 3.4.
"""

__author__ = "smiks"
__version__ = "0.8.3"


class Primes:
    """
    Class primarily meant for work with prime numbers.
    Finding primes, generating primes, prime factors and checking
    if certain number is prime.
    """

    def __init__(self):
        """
        Used only for cache. It saves first 1007 primes to object.
        These primes are later used as cache
        so it doesn't calculate first 1000 primes
        all over again.
        :return:
        """
        self.firstThousandPrimes = self.primesc(8000)

    @staticmethod
    def esieve(n):
        """
        Sieve of eratosthenes.
        :param n: Number to which you look for primes.
        Eg. n=10, returns all primes up to 10.
        :return: Returns dictionary number:boolean, where boolean presents
        if number is prime or not.
        """
        try:
            int(n)
        except ValueError:
            return {}
        primes = {i: (not(i <= 2 or i % 2 == 0)) for i in range(n+1)}
        primes[2] = True
        limit = sqrt(n) + 1
        i = 3
        while i <= limit:
            if primes[i]:
                j = 2 * i
                while j < n:
                    primes[j] = False
                    j += i
            i += 2
        return primes

    def primesc(self, n):
        """
        This function is used in __init__ to generate firstThousandPrimes
        :return:
        """
        try:
            int(n)
        except ValueError:
            return []
        return [i for i, j in self.esieve(n).items() if j]

    def first_n_primes(self, n):
        """
        Function is used for generating list of first n primes.
        :param n: Number, how many prime numbers you want.
        First N primes means, first starting with lowest natural number
        that is prime and up until you get N primes.
        :return: List of prime numbers.
        """
        try:
            int(n)
        except ValueError:
            return []
        if n < 0:
            return []
        if n <= 1000:
            return self.firstThousandPrimes[:n]
        primes = self.firstThousandPrimes[:1000]
        i = primes[999]
        counter = 1000
        while True:
            if counter == n:
                return primes
            if self.is_prime(i):
                primes.append(i)
                counter += 1
            i += 1
        return primes

    def prime_numbers(self, n):
        """
        Generates list of prime numbers below n.
        :param n: Number used as upper limit.
        All primes in a list are smaller than n.
        Eg. n=13, you get [2, 3, 5, 7, 11]
        :return: List of primes.
        """
        try:
            int(n)
        except ValueError:
            return []
        if n < 0:
            return []
        if n <= 7000:  # if n < 7000 definitely in firstThousandPrimes list
            return [i for i in self.firstThousandPrimes if i < n]
        return [i for i, j in self.esieve(n).items() if j]

    def primes_generator(self, n):
        """
        Generates prime numbers until prime number reaches n.
        :param n: Number used as upper limit.
        :return: Returns generator expression.
        In case of error, it returns empty list.
        """
        try:
            int(n)
        except ValueError:
            return []
        return (i for i, j in self.esieve(n).items() if j)

    def xprimes_generator(self):
        """
        Generates prime numbers.
        :return: Generated prime number.
        """
        counter = 1
        while True:
            if self.is_prime(counter):
                yield counter
            counter += 1

    def is_prime(self, p):
        """
        Function checks if n is prime number or not.
        This function is used as wrapper for Miller-Rabin
        to maintain backwards compatibility.
        :param p: Number to be checked if prime or not.
        :return: Returns boolean, True if number is prime otherwise False.
        """
        try:
            int(p)
        except ValueError:
            return -1

        if p < 1e7:
            if p < 2:
                return False
            if p == 2:
                return True
            if p > 2 and p%2 == 0:
                return False
            upper_bound = int(sqrt(p)+1)
            for i in range(3, upper_bound, 2):
                if p%i == 0:
                    return False
            return True

        return self.Miller_Rabin(p)

    def Miller_Rabin(self, n, k = 100):
        from random import randrange
        """
        Tries if n is prime in k passes of Miller-Rabin primality test.
        :param n: Number to be checked if prime.
        :param k: Number of rounds of Miller-Rabin test.
        :return: Returns True if number is prime, else False
        """
        small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 34, 47,
                        53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                        109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
                        173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
                        233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
                        293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
                        367, 373, 379, 383, 389, 397, 401, 409, 419, 419, 421,
                        431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                        491, 499, 503, 509, 521, 523, 541]
        if n < 2:
            return False

        for p in small_primes:
            if n < p * p:
                return True
            if n % p == 0:
                return False

        # taking care of some multipliers
        if n > 7 and (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0):
            return False

        # using cache to check first thousand primes
        if n in self.firstThousandPrimes:
            return True

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue

            for _ in range(r - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break
            else:
                return False
        return True


    def prime_factors(self, n):
        """
        Returns list of prime factors of number n.
        :param n: Number to be factorized.
        :return: List containing prime factors of number n.
        """
        try:
            int(n)
        except ValueError:
            return []
        factors = list()
        if self.is_prime(n):
            return [n]
        if (n // 2) > 1000:
            primelist = self.prime_numbers((n // 2) + 1)
        else:
            primelist = self.firstThousandPrimes
        for i in primelist:
            while n % i == 0:
                n = n // i
                factors.append(i)
            if n == 1:
                break
        return factors


class Numtools:
    """
    Contains functions for checking if number is pandigital,
    finding min and max element in a list, generating fibonacci numbers
    and counting divisors of given number.
    """

    @staticmethod
    def num_divisors(n):
        """
        Returns number of divisors (how many divisors) of number n
        """
        if n < 1:
            return 0
        if n == 1:
            return 1
        pfactors = Primes().prime_factors(n)
        divs = Counter(pfactors).values()
        return reduce(lambda x, y: x*y, [i+1 for i in divs])

    @staticmethod
    def pos(n):
        """
        :param n:
        :return:
        """
        if n == 0:
            return (0, 1)
        else:
            a, b = Numtools().pos(n / 2)
            c = a * (b * 2 - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)

    @staticmethod
    def fast_fib(n):
        """
        Returns nth fibonacci numbers.
        Also returns negative nth fibonacci numbers.
        :param n:
        :return:
        """
        def pos(n):
            if n == 0:
                return (0, 1)
            else:
                a, b = pos(n // 2)
                c = a * (b * 2 - a)
                d = a * a + b * b
                if n % 2 == 0:
                    return (c, d)
                else:
                    return (d, c + d)

        def fib(n):
            if n >= 0:
                return pos(n)[0]

            if n < 0:
                sign = -1 if n%2 == 0 else 1
                return sign*pos(abs(n))[0]

        return fib(n)

    @staticmethod
    def fibonacci_generator(n):
        """
        Generates n fibonacci numbers.
        :return: Fibonacci number.
        """
        try:
            int(n)
        except ValueError:
            return False
        a = b = 1
        for i in range(n):
            yield a
            a, b = b, a + b

    @staticmethod
    def find_minmax(lst):
        """
        Returns tuple with min and max element of a list.
        It finds both min and max element in O(n) (more exact: O(3/2n)
        """
        tmin = lst[0]
        tmax = lst[0]
        if len(lst) % 2 != 0:
            lst.append(lst[0])
        for i, j in zip(lst[0::2], lst[1::2]):
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
        return tmin, tmax

    @staticmethod
    def pandigitals_generator(lst):
        """
        Generates pandigital numbers from alphabet received as parameter lst
        :param lst: Alphabet used for pandigital numbers.
        :return: Pandigital number.
        """
        for i in lst:
            try:
                int(i)
            except ValueError:
                return []
        if any(i < 0 for i in lst):
            return -1
        for i in permutations(lst):
            yield int(''.join(map(str, i)))

    @staticmethod
    def is_pandigital(n, lst):
        """
        Function checks if given numebr n is pandigital
        considering given alphabet lst
        Eg. isPandigital(n, {1,2,3})
        it will check if n is pandigital number with digits 1, 2 and 3
        :return: Boolean, True if number is pandigital otherwise False
        """
        for i in lst:  # check if given alphabet is legit
            try:
                int(i)
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

    @staticmethod
    def is_signed_perm(lst):
        """
        Checks if given list (lst) is signed permutation.
        Eg.
        [5, 4, 3, 1] => False (missing 2)
        [1, 1, 2, 3] => False (1 appears twice)
        [1, 2, -3, 4] => True
        [1, 2, 3, 4, 5] => True
        Return: Boolean,
        True if lst represents signed permutation, otherwise False
        """
        dd = defaultdict(int)
        abslst = list(map(lambda x: abs(x), lst))
        llst = len(abslst)
        for i in abslst:
            dd[i] += 1
            if dd[i] > 1:
                return False
        if llst != max(abslst):
            return False
        return True

    @staticmethod
    def partial_permutation(n, k):
        """
        Function calculates partial permutation (where n>k) and returns result.
        """
        res = 1
        for i in range(n, n-k, -1):
            res *= i
        return res

    @staticmethod
    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k)*factorial(n-k))


class Joins:
    """
    Has function full_outer_join.
    """

    @staticmethod
    def full_outer_join(*matrices):
        """
        :param matrices: list of matrices
        :return: full outer join of given matrices
        """
        matrices = list(chain(*matrices))
        p = [i for i in product(*matrices)]
        ret = [list(chain(*i)) for i in p]
        return ret


class Sorts:
    """
    Counting Sort and Heap Sort and function is_sorted.
    Function is_sorted is good for checking if list is in ASC or DESC order.
    """

    @staticmethod
    def counting_sort(s, k=None):
        """
        CountingSort, used to sort integers in O(n+k)
        :param s: List to be sorted
        :param k: Number of buckets (algorithm generates k+1 buckets)
        :return:
        """
        if k is None:
            k = len(s)
        """ create k+1 buckets """
        nbuckets = k+1
        counter = [0 for _ in range(nbuckets)]
        for i in s:
            counter[i] += 1
        n = 0
        for i in range(nbuckets):
            while 0 < counter[i]:
                s[n] = i
                n += 1
                counter[i] -= 1
        return s

    @staticmethod
    def heap_sort(s):
        """
        Heap sort, sorts in O(nlogn)
        :param s: List to be sorted
        :return: Sorted list
        """
        heapify(s)
        return [heappop(s) for _ in range(len(s))]

    @staticmethod
    def is_sorted(s, order="ASC"):
        """
        Function checks if given list is sorted in O(n).
        :param s: List to be checked.
        :param order: What kind of order are we looking for. ASC or DESC
        :return:
        """
        prev = s[0]
        for i in s:
            if i < prev and order == "ASC":
                return False
            elif i > prev and order == "DESC":
                return False
            prev = i
        return True
