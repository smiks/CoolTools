from math import factorial, sqrt
from itertools import chain, permutations, product
from collections import Counter, defaultdict
from functools import reduce
from heapq import heapify, heappop

"""
Cooltools module has bunch of useful functions.
Module can be used for work with prime numbers, fibonacci sequence,
some basic operations on lists, pandigital numbers, calculating
jaccard index/distance on sets, algorithms on strings and calculating
some mathematical sums and series.
Passed compatibility tests for Python 3.4 and Python 3.5.
"""

__author__ = "smiks"
__version__ = "1.2"


class DimensionError(Exception):

    def __init__(self, message):
        self.message = message


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
                while j <= n:
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
            if p > 2 and p % 2 == 0:
                return False
            upper_bound = int(sqrt(p)+1)
            for i in range(3, upper_bound, 2):
                if p % i == 0:
                    return False
            return True

        return self.miller_rabin(p)

    def miller_rabin(self, n, k=100):
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

        # use Fermat to check composite numbers
        if pow(2, n-1, n) != 1:
            return False

        r, s = 0, n - 1
        while s % 2 == 0:
            r += 1
            s //= 2

        for _ in range(k):
            a = randrange(2, n - 1)
            x = pow(a, s, n)
            if x == 1 or x == n - 1:
                continue

            for __ in range(r - 1):
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
                sign = -1 if n % 2 == 0 else 1
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
    def partitions(n):
        """
        Function generates partitions of number n
        in an increasing order.
        Eg.:
        partitions(3) will yield
        [1, 1, 1]
        [1, 2]
        [3]
        """
        if n == 0:
            yield []
            return
        for p in Numtools.partitions(n - 1):
            yield [1] + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield [p[0] + 1] + p[1:]

    @staticmethod
    def digital_root(n):
        """
        Returns digital root of number n.
        :param n: integer
        """
        return 1+((n-1) % 9) if n > 0 else 0

    @staticmethod
    def total_inc_dec(d):
        """
        Function returns how many numbers up to 10^d are there
        that are increasing or decreasing.
        Increasing number:
            number where each digit is same or bigger compared to previous.
            eg. 1123, 12345, 189999, 444

        Decreasing number:
            number where each digit is same or lower compared to previous.
            eg. 2211, 654321, 88764421000, 444

        :param d: Number of digits

        :return: Total amount of increasing and decreasing numbers up to 10^d
        """
        map_ = {
            0: 1,
            1: 10,
            2: 100,
            3: 475,
            4: 1675,
            5: 4594,
            6: 12952,
            7: 30817,
            8: 67987,
            9: 140907,
            10: 277033
        }
        if d in map_:
            return map_[d]

        bc = Math.binomial_coefficient

        # there is x*10 numbers that are both INC and DESC
        return bc(d+10, 10) + bc(d+9, 9) - 1 - d*10


    @staticmethod
    def compare_floats(a, b, eps=1e-6):
        """
        Returns True if numbers a and b are close enough to be considered as same
        otherwise returns False
        :param a: float
        :param b: float
        :param eps: float
        :return:
        """
        if abs(a - b) < eps:
            return True
        return False

    @staticmethod
    def frange(a, b, s=0.5):
        """
        Similar to range generator. It works with floats.
        :param a: Starting point
        :param b: End point
        :param s: step (can be float)
        :return:
        """
        while a < b:
            yield  a
            a += s

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


class Math:
    """
        Math class contains some mathematical functions.
    """

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

    @staticmethod
    def sum_arithmetic_series(b, a=1):
        """
        Function returns sum of arithmetic series from a to b.
        :param b: upper bound
        :param a: lower bound, [default = 1]
        :return: sum of arithmetic series from a to b.
        """

        if b < 0:
            raise ValueError("Argument b should be non-negative integer!")

        if b == 0:
            return 0

        """ from 1 to b """
        part_b = (b * (b + 1)) // 2

        if a == 1:
            return part_b

        """ from a to b """
        part_a = (a * (a + 1)) // 2

        return part_b - part_a + a

    @staticmethod
    def sum_arithmetic_progression(min_, max_, step):
        """
        Function returns arithmetic progression sum.
        Function works correctly only if all numbers are part
        of same arithmetic progression.
        sum = n(a1+an)/ 2
        :param min_: Smallest number in progression.
        :param max_: Biggest number in progression.
        :param step: Absolute difference between two adjacent number
        :return: Sum of arithmetic progression
        """
        lst = sum(1 for _ in range(min_, max_+1, step))
        return (lst*(min_ + max_)) >> 1

    @staticmethod
    def sum_square_series(b, a=1):
        """
        Function returns sum of square series from a to b.
        :param b: upper bound
        :param a: lower bound, [default = 1]
        :return: sum of square series from a to b.
        """

        if b < 0:
            raise ValueError("Argument b should be non-negative integer!")

        if b == 0:
            return 0

        """ from 1 to b """
        """
            (n * (n+1) * (2n+1)) / 6 =
            (2n^3 + 3n^2 + n) / 6
        """
        part_b = (2*b**3 + 3*b**2 + b) / 6

        if a == 1:
            return int(part_b)

        part_a = (2*a**3 + 3*a**2 + a) / 6

        return int(part_b - part_a + a**2)

    @staticmethod
    def sum_cubic_series(b, a=1):
        """
        Function returns sum of cubic series from a to b.
        :param b: upper bound
        :param a: lower bound, [default = 1]
        :return: sum of cubic series from a to b.
        """
        if b < 0:
            raise ValueError("Argument b should be non-negative integer!")

        if b == 0:
            return 0

        """ from 1 to b """
        part_b = (b**2 * (b+1)**2) >> 2

        if a == 1:
            return int(part_b)

        part_a = (a**2 * (a+1)**2) >> 2

        return int(part_b - part_a + a**3)

    @staticmethod
    def sum_tetrahedral_series(b, a=1):
        """
        Function returns sum of tetrahedral series from a to b.
        :param b: upper bound
        :param a: lower bound, [default = 1]
        :return: sum of cubic series from a to b.
        """
        if b < 0:
            raise ValueError("Argument b should be non-negative integer!")

        if b == 0:
            return 0

        """ from 1 to b """
        part_b = (b * (b+1) * (b+2)) / 6

        if a == 1:
            return int(part_b)

        a -= 1
        part_a = (a * (a+1) * (a+2)) / 6

        return int(part_b - part_a)

    @staticmethod
    def manhattan_distance(point_a, point_b):
        """
        Function returns manhattan distance between point A and point B.
        Example:
            manhattan_distance((1,2,3), (4,5,6))

        :param point_a: tuple with coordinates of pointA
        :param point_b: tuple with coordinates of pointB
        :return:
                Function returns manhattan distance between point A and point B.
        """
        if len(point_a) != len(point_b):
            raise DimensionError("Number of dimensions of point A is "
                                 "not same as number of dimensions of point B.")

        return sum(abs(a - b) for a, b in zip(point_a, point_b))

    @staticmethod
    def euclidean_distance(pointa_a, point_b):
        """
        Function returns Euclidean distance between point A and point B.
        Example:
            euclidean_distance((1,2,3), (4,5,6))

        :param pointa_a: tuple with coordinates of pointA
        :param point_b: tuple with coordinates of pointB
        :return:
                Function returns Euclidean distance between point A and point B.
        """

        from math import sqrt

        if len(pointa_a) != len(point_b):
            raise DimensionError("Number of dimensions of point A is "
                                 "not same as number of dimensions of point B.")

        return sqrt(sum((a - b)**2 for a, b in zip(pointa_a, point_b)))

    @staticmethod
    def fact_sum_divby_fact(n):
        """
        Function returns
                  _n_
        1 / n!    \    i!
                  /__
                   i=1
        :param n: integer and upper limit
        :return: Result of 1/n!  *  sum(i! for i in range(1,n+1))
        """
        from itertools import accumulate
        from operator import mul
        return sum(accumulate((1.0/i for i in range(n, 1, -1)), mul))+1

    @staticmethod
    def euler_totient(n):
        """
        Euler's totient function
        :param n: integer n
        :return: Returns result of Euler's totient function
        """
        res = 1.0 * n
        p = 2
        while p * p <= n:
            if n % p == 0:
                while n % p == 0:
                    n = n / p
                res *= (1.0 - (1.0 / p))
            p += 1

        if n > 1:
            res *= (1.0 - (1.0 / n))

        return int(res)

    @staticmethod
    def reduced_fractions(d):
        """
        Returns how many proper fractions are between
        0/d and d/d.
        Proper fraction: gcd(numerator, denominator) == 1
        :param d: integer, denominator
        :return: Number of proper fractions.
        """
        if d == 1:
            return 0
        return Math.euler_totient(d)

    @staticmethod
    def left_riemann_sum(f, n, a, b):
        """
        Returns left Riemann sum of function 'f'
        with 'n' rectangles from 'a' to 'b'.

        zero_fix is used to avoid division by 0
        :param f: function with single argument  f(x)
        :param n: number of rectangles
        :param a: lower bound
        :param b: upper bound
        :return:
        """
        zero_fix = 1e-16
        dx = (b-a)/n
        return sum(dx*f(xi+zero_fix) for xi in Numtools.frange(a, b, dx))

    @staticmethod
    def right_riemann_sum(f, n, a, b):
        """
        Returns right Riemann sum of function 'f'
        with 'n' rectangles from 'a' to 'b'

        zero_fix is used to avoid division by 0
        :param f: function with single argument  f(x)
        :param n: number of rectangles
        :param a: lower bound
        :param b: upper bound
        :return:
        """
        zero_fix = 1e-16
        dx = (b-a)/n
        return sum(dx*f(xi+dx+zero_fix) for xi in Numtools.frange(a, b, dx))

    @staticmethod
    def trapezoidal_rule(f, n, a, b, abs_=False):
        """
        Returns average of left and right Riemann sum of function 'f'
        with 'n' rectangles from 'a' to 'b'.
        Average is same as trapezoidal rule.

        zero_fix is used to avoid division by 0
        :param f: function with single argument  f(x)
        :param n: number of rectangles
        :param a: lower bound
        :param b: upper bound
        :param abs_: flag if you want to calculate absolute area or not
        :return:
        """
        zero_fix = 1e-16
        dx = (b-a)/n
        s = 0
        cache = dict()
        for xi in Numtools.frange(a, b, dx):

            if xi+dx+zero_fix in cache:
                l = cache[xi+dx+zero_fix]
            else:
                l = dx*f(xi+zero_fix)

            r = dx*f(xi+dx+zero_fix)

            if xi+dx+zero_fix not in cache:
                cache[xi+dx+zero_fix] = r

            a = (l+r)/2
            s += abs(a) if abs_ else a
        return s

    @staticmethod
    def converg_approx_area(f, a, b, eps=1e-4, max_step=10, abs_=False):
        """
        Funcion uses trapezoidal_rule with different 'n's.
        Keeps increasing number of 'n's until difference between last two
        calculations is less than 'eps'.

        zero_fix is used to avoid division by 0

        Time complexity: O(2^n) where n represents how many times function f is
        evaluated, which is n ~ 2^max_step

        :param f: function with single argument  f(x)
        :param a: lower bound
        :param b: upper bound
        :param eps: convergence limit
        :param max_step: how many steps before forced stop.
            Each step doubles number of trapezoids ('n's).
        :param abs_: flag if you want to calculate absolute area or not
        :return:
        """

        n = 1
        prev = 0
        while max_step > 0:
            curr = Math.trapezoidal_rule(f, n, a, b, abs_=abs_)
            diff = abs(prev - curr)

            if diff < eps:
                return curr

            n = n<<1
            max_step -= 1
            prev = curr

        return curr


class Algorithms:
    """
        Various algorithms on strings, sets etc...
    """

    @staticmethod
    def jaccard_index(set_a, set_b):
        """
        Function calculates Jaccard index (similarity) between two sets.
        :param set_a: set
        :param set_b: set
        :return: Jaccard index between sets (setA and setB).
        """
        union = set_a | set_b
        inter = set_a & set_b

        return len(inter) / len(union)

    @staticmethod
    def jaccard_distance(set_a, set_b):
        """
        Function calculates Jaccard distance between two sets.
        Function calls jaccard_index function.
        :param set_a: set
        :param set_b: set
        :return: Jaccard distance between sets (setA and setB).
        """
        return 1 - Algorithms.jaccard_index(set_a, set_b)

    @staticmethod
    def lcs(s1, s2):
        """
        Function returns longest common substring.
        :param s1: string
        :param s2: string
        :return: String which is longest common substring.
        """
        from collections import defaultdict

        def lcss(s, t):

            def match_score(a, b):
                return 1 if a == b else -2

            m = defaultdict(int)  # initialization (matrix M)
            prev = dict()
            for i, si in enumerate(s):
                for j, tj in enumerate(t):
                    m[i, j], prev[i, j] = max(
                        (m[i - 1, j - 1] + match_score(si, tj), (i - 1, j - 1)),  # match
                        (m[i - 1, j], (i - 1, j)),  # delete - leave same score
                        (m[i, j - 1], (i, j - 1))  # insert - leave same score
                    )
            return m, prev

        def traceback(s, t, table, prev):
            i, j = len(s) - 1, len(t) - 1
            res = ""
            while table[i, j] != 0:
                if prev[i, j] == (i - 1, j - 1):
                    res = s[i] + res
                i, j = prev[i, j]
            return res

        m, prev = lcss(s1, s2)
        res = traceback(s1, s2, m, prev)

        return res

    @staticmethod
    def levenshtein_distance(s_a, s_b):
        """
        Function calculates Levenshtein distance -
                                                similarity between two strings.
        :param s_a: String A.
        :param s_b: String B.
        :return: Returns Levenshtein distance between two strings.
        """

        # Let's assume sA will always be longer
        if len(s_a) < len(s_b):
            return Algorithms.levenshtein_distance(s_b, s_a)

        if len(s_b) == 0:
            return len(s_a)

        prev_row = range(len(s_b) + 1)
        for i, cA in enumerate(s_a):
            curr_row = [i + 1]
            for j, cB in enumerate(s_b):
                curr_row.append(min(
                    prev_row[j + 1] + 1,  # insert
                    curr_row[j] + 1,  # delete
                    prev_row[j] + (cA != cB)  # substitute
                ))

            prev_row = curr_row

        return prev_row[-1]

    @staticmethod
    def substring_counter(string, substring):
        """
        Function is version of python count() function.
        Difference is that this function counts differently.
            Example:
                String: CCC
                Count: CC
                "CCC".count("CC")  # returns 1
                substring_counter("CCC", "CC")  # returns 2
        :param string: Main string.
        :param substring: What substring will be checked.
        :return: Counts occurrence of substring in main string.
            Returns -1 if string is empty but substring is not.
            Returns 1 if both strings are empty
            Returns 0 if string is empty but substring is not.
            In other cases, it returns counted occurrences.
        """

        if len(substring) == 0 and len(string) == 0:
            return 1

        if len(substring) == 0:
            return 0

        if len(string) == 0:
            return -1

        len_str = len(string)
        len_sub = len(substring)
        return sum(
            1 if string[i:i+len_sub] == substring else 0
            for i in range(len_str-len_sub + 1)
        )

    @staticmethod
    def kmp(string, pattern):
        """
        Knuth-Morris-Pratt algorithm
        Finding occurrence of substring (pattern) in a larger string.
        If substring occurs in a larger string, function returns start position
        (index in a larger string), if it does not occur function returns -1.
        If either string or pattern is empty, function returns -1.

        :param string: string (Larger string)
        :param pattern: string (Substring)
        :return:
            start position or -1 if substring does not occur in a larger string.
        """

        # either string or pattern is empty, return -1
        if len(string) * len(pattern) == 0:
            return -1

        # build table of shifts
        pattern = list(pattern)
        lp = len(pattern)
        shifts = [1] * (lp + 1)
        shift = 1
        for p in range(lp):
            while shift <= p and pattern[p] != pattern[p - shift]:
                shift += shifts[p - shift]
            shifts[p + 1] = shift

        # search
        start_pos = 0
        match_len = 0
        for c in string:
            while match_len == lp or \
                                    match_len >= 0 and pattern[match_len] != c:
                start_pos += shifts[match_len]
                match_len -= shifts[match_len]

            match_len += 1

            if match_len == lp:
                return start_pos

        return -1

    @staticmethod
    def find_word(board, word):
        """
        Function returns True if word occures in a board or Fales if it
        does not. Function works in a same way as game Boggle/Scramble.
        :param board: list of lists (2D matrix with letters)
        :param word: string (Word to be checked)
        :return: If word exists in a board returns True otherwise False.
        """
        from collections import defaultdict as dd

        x = [-1, -1, -1, 0, 0, 1, 1, 1]
        y = [-1, 0, 1, -1, 1, -1, 0, 1]
        taken = dd(bool)

        def search(grid, pos_x, pos_y, curr_index, word, taken):
            if curr_index == len(word):
                return True

            to_look = word[curr_index]

            """ check neighbours """
            for d in range(8):
                rd = pos_x + x[d]
                cd = pos_y + y[d]

                if rd < 0 or rd >= len(grid) or cd < 0 or cd >= len(grid[0]):
                    continue

                if not taken[(rd, cd)] and grid[rd][cd] == to_look:
                    old_taken = taken
                    taken[(rd, cd)] = True
                    if search(grid, rd, cd, curr_index+1, word, taken):
                        return True
                    taken = old_taken

        """ find first occurrence """
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    taken[(row, col)] = True
                    if len(word) == 1:
                        return True

                    if search(board, row, col, 1, word, taken):
                        return True
                    else:
                        taken = dd(bool)

        return False

    @staticmethod
    def find_rot_index(l):
        """
        Function returns index of first element that is rotated and
        order (1: ASC, -1: DESC).
        If list is not rotated function will return -1 for index.
        :param l: list with numbers
        :return: Index of first element that is rotated and order
        """

        # lists with length less than 3 can't be rotated
        if len(l) < 3:
            return -1

        # detect ASC or DESC (1: ASC, -1: DESC)
        order = 1
        if l[0] < l[-1]:
            order = -1

        # check if rotated at all (if not, return 0)
        if (l[0] < l[1] < l[-1]) or (l[0] > l[1] > l[-1]):
            order = 1 if l[0] < l[1] else -1
            return -1, order

        # find rotation index (if rotated return index of position)
        def rot(left, right):
            mid = (left + right) // 2

            # check if found
            if left == mid and l[mid] > l[right] and order == 1:  # odd length fix
                return mid

            if left == mid and l[mid] < l[right] and order == -1:  # odd length fix
                return mid

            if order == 1 and abs(mid - left) == 1:
                return mid if l[left] > l[mid] else right

            if order == -1 and abs(mid - left) == 1:
                return mid if l[mid] > l[left] else right

            # next round
            if order == 1 and l[mid] > l[right]:
                return rot(mid, right)

            if order == 1 and l[mid] < l[right]:
                return rot(left, mid)

            if order == -1 and l[mid] < l[right]:
                return rot(mid, right)

            if order == -1 and l[mid] > l[right]:
                return rot(left, mid)

        return rot(0, len(l) - 1), order

    @staticmethod
    def two_sum(lst, n):
        """
        Function returns pair of numbers which sum is n.
        Time complexity: O(n)
        Space complexity: O(n)
        :param lst: list of numbers
        :param n: number (sum of two)
        :return: tuple (pair of numbers which sum is n)
        If there is no such pair, function returns None
        """
        seen = set()
        needed = set()
        results = []
        for i in lst:
            seen.add(i)
            needed.add(n-i)
            if i in needed and n-i in seen:
                results.append(sorted([i, n-i]))

        return results if len(results) > 0 else None

    @staticmethod
    def max_subarray_sum(lst):
        """
        Function receives list of numbers
        and returns maximum contiguous subarray sum
        :param lst: list of numbers
        :return: aximum contiguous subarray sum
        """
        max_ = lst[0]
        curr = lst[0]
        for i in lst[1:]:
            curr = max(i, curr+i)
            max_ = max(max_, curr)

        return max_

    @staticmethod
    def lis(lst):
        """
        Longest Increasing Subsequence
        Function returns list which represents longest
        increasing subsequence of list lst.
        :param lst: list with numbers
        :return: list (longest increasing subsequnce)
        """
        l = []
        for i in range(len(lst)):
            l.append(
                max( [l[j] for j in range(i) if l[j][-1] < lst[i]] or [[]],
                     key=len )
                 + [lst[i]]
            )

        return max(l, key=len)

    @staticmethod
    def kth_smallest(l, k):
        """
        Returns k-smallest element. Ignores duplicates.
        Starts counting with 1 (not zero).
        Time complexity O(n)
        :param l: list with numbers
        :param k: integer k-th smallest
        :return: return k-th smallest element in the list
        """
        _l = list({i for i in l})
        heapify(_l)
        if k < 1 or len(l) == 0 or k > len(_l):
            return None
        ret = 0
        for _ in range(k):
            ret = heappop(_l)

        return ret

    @staticmethod
    def smallest_positive_missing(l):
        """
        Returns smallest positive number missing in a list 'l'.
        Only works with integers.
        Time complexity: O(n)
        Space complexity: O(n)
        :param l: List with integers
        :return: smallest positive number missing in a list.
        """
        if len(l) == 0:
            return 1
        seen = set()
        max_ = l[0]
        for el in l:
            if el > 0:
                seen.add(el)
                max_ = max(max_, el)

        for i in range(1, max_):
            if i not in seen:
                return i

        return max_+1
