__author__ = 'smiks'
import unittest
from cooltools import *


class Tests(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(Primes().first_n_primes(10), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test first 10 primes")
        self.assertTrue(Primes().is_prime(2), "Test if 2 is prime")
        self.assertTrue(Primes().is_prime(3), "Test if 3 is prime")
        self.assertFalse(Primes().is_prime(14), "Test if 14 is prime")
        self.assertTrue(Primes().is_prime(23), "Test if 23 is prime")
        self.assertTrue(Primes().is_prime(31), "Test if 31 is prime")
        self.assertTrue(Primes().is_prime(15485863), "Test if 15485863 is prime")
        self.assertTrue(Primes().is_prime(32416190071), "Test if 32416190071 is prime")
        self.assertFalse(Primes().is_prime(1247), "Test if 1247 is prime")
        self.assertFalse(Primes().is_prime(30143), "Test if 30143 is prime")
        self.assertEqual(Primes().prime_factors(10), [2, 5], "Test prime factors of number 10")
        self.assertEqual(Primes().prime_factors(13), [13], "Test prime factors of number 10")

    def test_nums(self):
        self.assertEqual(Numtools().num_divisors(10), 4, "Testing how many divisors has number 10")
        self.assertEqual(Numtools().fast_fib(5), 5, "Testing 5th fibonacci number should be 5")
        self.assertEqual(Numtools().fast_fib(6), 8, "Testing 6th fibonacci number should be 8")
        self.assertEqual(Numtools().fast_fib(10), 55, "Testing 10th fibonacci number should be 55")
        self.assertEqual(Numtools().fast_fib(0), 0, "Testing 0th fibonacci number should be 0")
        self.assertEqual(Numtools().fast_fib(-5), 5, "Testing -5th fibonacci number should be 5")
        self.assertEqual(Numtools().fast_fib(-6), -8, "Testing -6th fibonacci number should be -8")
        fibs = [i for i in Numtools.fibonacci_generator(10)]
        res = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(fibs, res, "Testing first 10 fibonacci numbers")
        self.assertEqual(Numtools.find_minmax([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]), (2, 29),
                         "Testing min and max in a list")
        self.assertTrue(Numtools.is_pandigital(234, [2, 3, 4]), "Testing if 234 is pandigital in alphabet [2,3,4]")
        self.assertFalse(Numtools.is_pandigital(234, [2, 3, 2]), "Testing if 232 is pandigital in alphabet [2,3,4]")
        self.assertTrue(Numtools.is_signed_perm([1, 2, 3, 4, 5]), "Testing signed permutation")
        self.assertTrue(Numtools.is_signed_perm([1, -2, -3, 4, 5]), "Testing signed permutation")
        self.assertTrue(Numtools.is_signed_perm([-1, -2, -3, -4, -5]), "Testing signed permutation")
        self.assertFalse(Numtools.is_signed_perm([1, 2, 2, 4, 5]), "Testing signed permutation")
        self.assertFalse(Numtools.is_signed_perm([1, 2, 4, 5]), "Testing signed permutation")
        self.assertFalse(Numtools.is_signed_perm([-1, -2, -2, 4, 5]), "Testing signed permutation")
        self.assertFalse(Numtools.is_signed_perm([-1, -2, 4, 5]), "Testing signed permutation")
        self.assertEqual(Numtools.partial_permutation(21, 7), 586051200, "Testing partial permutation")
        self.assertEqual(Numtools.binomial_coefficient(21, 7), 116280, "Testing binomial coefficient")


    def test_joins(self):
        m1 = [['+', '-']]
        m2 = [['1', '2', '3'], ['4', '5', '6']]
        m3 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
        m1 = [['+'], ['-']]
        m2 = [['1'], ['2'], ['3']]
        m3 = [['a'], ['b'], ['c']]
        m4 = [['X'], ['Z']]
        matrices = [m1, m2, m3, m4]
        self.assertEqual(Joins.full_outer_join(matrices), [['+', '1', 'a', 'X'], ['+', '1', 'a', 'Z'],
                                                           ['+', '1', 'b', 'X'], ['+', '1', 'b', 'Z'],
                                                           ['+', '1', 'c', 'X'], ['+', '1', 'c', 'Z'],
                                                           ['+', '2', 'a', 'X'], ['+', '2', 'a', 'Z'],
                                                           ['+', '2', 'b', 'X'], ['+', '2', 'b', 'Z'],
                                                           ['+', '2', 'c', 'X'], ['+', '2', 'c', 'Z'],
                                                           ['+', '3', 'a', 'X'], ['+', '3', 'a', 'Z'],
                                                           ['+', '3', 'b', 'X'], ['+', '3', 'b', 'Z'],
                                                           ['+', '3', 'c', 'X'], ['+', '3', 'c', 'Z'],
                                                           ['-', '1', 'a', 'X'], ['-', '1', 'a', 'Z'],
                                                           ['-', '1', 'b', 'X'], ['-', '1', 'b', 'Z'],
                                                           ['-', '1', 'c', 'X'], ['-', '1', 'c', 'Z'],
                                                           ['-', '2', 'a', 'X'], ['-', '2', 'a', 'Z'],
                                                           ['-', '2', 'b', 'X'], ['-', '2', 'b', 'Z'],
                                                           ['-', '2', 'c', 'X'], ['-', '2', 'c', 'Z'],
                                                           ['-', '3', 'a', 'X'], ['-', '3', 'a', 'Z'],
                                                           ['-', '3', 'b', 'X'], ['-', '3', 'b', 'Z'],
                                                           ['-', '3', 'c', 'X'], ['-', '3', 'c', 'Z']],
                         "Testing full outer join")

    def test_sorts(self):
        self.assertEqual(Sorts.counting_sort([1, 3, 2, 4, 6, 5, 2, 7]), [1, 2, 2, 3, 4, 5, 6, 7], "Testing counting sort")
        self.assertEqual(Sorts.counting_sort([7, 6, 5, 4, 3, 2], 7), [2, 3, 4, 5, 6, 7], "Testing counting sort")
        self.assertEqual(Sorts.counting_sort([1, 1, 1, 1, 1, 1], 2), [1, 1, 1, 1, 1, 1], "Testing counting sort")
        self.assertEqual(Sorts.heap_sort([1, 3, 2, 4, 6, 5, 2, 7]), [1, 2, 2, 3, 4, 5, 6, 7], "Testing heap sort")
        self.assertEqual(Sorts.heap_sort([7, 6, 5, 4, 3, 2]), [2, 3, 4, 5, 6, 7], "Testing heap sort")
        self.assertEqual(Sorts.heap_sort([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1], "Testing heap sort")
        self.assertTrue(Sorts.is_sorted([1, 1, 1, 1, 1, 1]), "Testing if list is sorted ASC")
        self.assertTrue(Sorts.is_sorted([1, 2, 3, 4, 5, 6]), "Testing if list is sorted ASC")
        self.assertTrue(Sorts.is_sorted([1, 2, 3, 4, 5, 6], order="ASC"), "Testing if list is sorted ASC")
        self.assertTrue(Sorts.is_sorted([1, 1, 1, 1, 1, 1], order="DESC"), "Testing if list is sorted DESC")
        self.assertTrue(Sorts.is_sorted([6, 5, 4, 3, 2, 1], order="DESC"), "Testing if list is sorted DESC")
        self.assertFalse(Sorts.is_sorted([4, 2, 1, 5, 6, 7], order="ASC"), "Testing if list is not sorted ASC")
        self.assertFalse(Sorts.is_sorted([4, 2, 1, 5, 6, 7], order="DESC"), "Testing if list is not sorted DESC")
        self.assertFalse(Sorts.is_sorted([6, 5, 4, 3, 2, 1], order="ASC"), "Testing if list is not sorted ASC")
        self.assertFalse(Sorts.is_sorted([1, 2, 3, 4, 5, 6], order="DESC"), "Testing if list is not sorted DESC")


if __name__ == "__main__":
    tests = Tests()
    tests.test_primes()
    tests.test_nums()
    tests.test_joins()
    tests.test_sorts()
