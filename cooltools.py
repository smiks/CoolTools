"""
Cooltools module has bunch of useful functions.
Module can be used for work with prime numbers, fibonacci sequence,
some basic operations on lists and pandigital numbers.
"""

__author__ = "smiks"
__version__ = "0.7.5"

from math import sqrt
from itertools import permutations, product, chain
from collections import defaultdict
from functools import reduce
from collections import Counter
from heapq import heapify, heappop


class Primes:
    """
    Class primarily meant for work with prime numbers.
    Finding primes, generating primes, prime factors and checking
    if certain number is prime.
    """

    def __init__(self):
        """
        Used only for cache. It saves first 1007 primes to object.
        These primes are later used as cache so it doesn't calculate first 1000 primes
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
        primes = {i: (not(i == 2 or i % 2 == 0 or i == 0 or i == 1)) for i in range(n+1)}
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

    def primes(self, n):
        """
        Generates list of prime numbers below n.
        :param n: Number used as upper limit. All primes in a list are smaller than n.
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

    def is_prime(self, n):
        """
        Function checks if n is prime number or not.
        :param n: Number to be checked if prime or not.
        :return: Returns boolean, True if number is prime otherwise False.
        """
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
        if n > 11 and \
                (n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0 or n % 11 == 0):
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
            primelist = self.primes((n // 2) + 1)
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
        pfactors = primes.prime_factors(n)
        divs = Counter(pfactors).values()
        return reduce(lambda x, y: x*y, [i+1 for i in divs])

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
        Eg. isPandigital(n, {1,2,3}) it will check if n is pandigital number with digits 1, 2 and 3
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
    Has two sorting algorithms, Counting Sort and Heap Sort and function is_sorted.
    Function is_sorted is good for checking if list is in ASC or DESC order.
    """

    @staticmethod
    def counting_sort(s, k):
        """
        CountingSort, used to sort integers in O(n+k)
        :param s: List to be sorted
        :param k: Number of buckets (algorithm generates k+1 buckets)
        :return:
        """
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


if __name__ == "__main__":
    from random import randint
    print("TESTING")

    ''' testing primes '''
    primes = Primes()
    a = 10
    fnprimes = primes.first_n_primes(a)
    print("First ", a, " primes")
    print(fnprimes)
    print("Testing if 2 and 4 are primes: ", primes.is_prime(2), primes.is_prime(4))
    print("Testing function primes(13): ", end="")
    print(primes.primes(13))
    print("Testing prime factors of 10 and 13: ", primes.prime_factors(10), primes.prime_factors(13))
    ''' testing numtools '''
    nums = Numtools()
    a = 10
    ndiv = nums.num_divisors(a)
    print(a, " has ", ndiv, " divisors")
    print("Generating fibonacci numbers n:10")
    for i in nums.fibonacci_generator(10):
        print(i, end=", ")
    print()
    print("Finding min and max in list: ", fnprimes)
    print(nums.find_minmax(fnprimes))
    print()
    print("Testing if numbers 234 and 232 are pandigital numbers ", nums.is_pandigital(234, [2,3,4]),
                                                                    nums.is_pandigital(232, [2,3,4]))
    print()
    ''' testing joins '''
    Join = Joins()
    m1 = [['+', '-']]
    m2 = [['1', '2', '3'], ['4', '5', '6']]
    m3 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
    m1 = [['+'], ['-']]
    m2 = [['1'], ['2'], ['3']]
    m3 = [['a'], ['b'], ['c']]
    m4 = [['X'], ['Z']]

    matrices = [m1, m2, m3, m4]
    res = Join.full_outer_join(matrices)
    for i in res:
        print(i)

    ''' testing sorts '''
    unsorted = [randint(1, 50) for i in range(50)]
    sorts = Sorts()
    sort = sorts.heap_sort(unsorted[::])
    if sort == sorted(unsorted):
        print("List is sorted using heap sort")
    else:
        print("List is NOT sorted (using heapsort)")

    if not sorts.is_sorted(unsorted):
        print("Unsorted list is not sorted")
    if sorts.is_sorted(sort):
        print("Sorted list is sorted")
    if sorts.is_sorted(sort) and sort == sorted(sort):
        print("Looks like isSorted works")

    sort = sorts.counting_sort(unsorted, len(unsorted))
    if sort == sorted(unsorted):
        print("List is sorted using counting sort")
    else:
        print("List is NOT sorted (using counting sort)")

    rfnprimes = fnprimes[::-1]
    print("Checking if list ", rfnprimes, " is sorted DESC")
    print(sorts.is_sorted(rfnprimes, order="DESC"))
    print("Checking if list ", rfnprimes, " is sorted ASC")
    print(sorts.is_sorted(rfnprimes, order="ASC"))