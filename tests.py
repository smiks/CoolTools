__author__ = 'smiks'
import unittest
from cooltools import *


class Tests(unittest.TestCase):
    def test_primes(self):
        self.assertEqual(
            Primes().first_n_primes(10),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29],
            "Test first 10 primes"
        )
        self.assertTrue(
            Primes().is_prime(2),
            "Test if 2 is prime"
        )
        self.assertTrue(
            Primes().is_prime(3),
            "Test if 3 is prime"
        )
        self.assertFalse(
            Primes().is_prime(14),
            "Test if 14 is prime"
        )
        self.assertTrue(
            Primes().is_prime(23),
            "Test if 23 is prime"
        )
        self.assertTrue(
            Primes().is_prime(31),
            "Test if 31 is prime"
        )
        self.assertTrue(
            Primes().is_prime(15485863),
            "Test if 15485863 is prime"
        )
        self.assertTrue(
            Primes().is_prime(32416190071),
            "Test if 32416190071 is prime"
        )
        self.assertFalse(
            Primes().is_prime(10000000000000000034000000000000000011739),
            "Test if 10000000000000000034000000000000000011739 is composite"
        )
        self.assertTrue(
            Primes().is_prime(32416186963),
            "Test if 32416190071 is prime"
        )
        self.assertTrue(
            Primes().is_prime(32416186093),
            "Test if 32416186093 is prime"
        )
        self.assertFalse(
            Primes().is_prime(1247),
            "Test if 1247 is prime"
        )
        self.assertFalse(
            Primes().is_prime(30143),
            "Test if 30143 is prime"
        )
        self.assertEqual(
            Primes().prime_factors(10),
            [2, 5],
            "Test prime factors of number 10"
        )
        self.assertEqual(
            Primes().prime_factors(13),
            [13],
            "Test prime factors of number 10"
        )

    def test_nums(self):
        self.assertEqual(
            Numtools().num_divisors(10),
            4,
            "Testing how many divisors has number 10"
        )
        self.assertEqual(
            Numtools().fast_fib(5),
            5,
            "Testing 5th fibonacci number should be 5"
        )
        self.assertEqual(
            Numtools().fast_fib(6),
            8,
            "Testing 6th fibonacci number should be 8"
        )
        self.assertEqual(
            Numtools().fast_fib(10),
            55,
            "Testing 10th fibonacci number should be 55"
        )
        self.assertEqual(
            Numtools().fast_fib(0),
            0,
            "Testing 0th fibonacci number should be 0"
        )
        self.assertEqual(
            Numtools().fast_fib(-5),
            5,
            "Testing -5th fibonacci number should be 5"
        )
        self.assertEqual(
            Numtools().fast_fib(-6),
            -8,
            "Testing -6th fibonacci number should be -8"
        )

        fibs = [i for i in Numtools.fibonacci_generator(10)]
        res = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        self.assertEqual(
            fibs,
            res,
            "Testing first 10 fibonacci numbers"
        )
        self.assertEqual(
            Numtools.find_minmax([2, 3, 5, 7, 11, 13, 17, 19, 23, 29]),
            (2, 29),
            "Testing min and max in a list"
        )
        self.assertTrue(
            Numtools.is_pandigital(234, [2, 3, 4]),
            "Testing if 234 is pandigital in alphabet [2,3,4]"
        )
        self.assertFalse(
            Numtools.is_pandigital(234, [2, 3, 2]),
            "Testing if 232 is pandigital in alphabet [2,3,4]"
        )
        self.assertTrue(
            Numtools.is_signed_perm([1, 2, 3, 4, 5]),
            "Testing signed permutation"
        )
        self.assertTrue(
            Numtools.is_signed_perm([1, -2, -3, 4, 5]),
            "Testing signed permutation"
        )
        self.assertTrue(
            Numtools.is_signed_perm([-1, -2, -3, -4, -5]),
            "Testing signed permutation"
        )
        self.assertFalse(
            Numtools.is_signed_perm([1, 2, 2, 4, 5]),
            "Testing signed permutation"
        )
        self.assertFalse(
            Numtools.is_signed_perm([1, 2, 4, 5]),
            "Testing signed permutation"
        )
        self.assertFalse(
            Numtools.is_signed_perm([-1, -2, -2, 4, 5]),
            "Testing signed permutation"
        )
        self.assertFalse(
            Numtools.is_signed_perm([-1, -2, 4, 5]),
            "Testing signed permutation"
        )

        partitions_n = 4
        partitions_correct = [[1, 1, 1, 1], [1, 1, 2], [2, 2], [1, 3], [4]]
        for p in Numtools.partitions(partitions_n):
            self.assertTrue(p in partitions_correct, "Test if partitions work")

        self.assertEqual(
            Numtools.total_inc_dec(11),
            520565,
            "Testing 10^100 inc_dec numbers."
        )

        self.assertEqual(
            Numtools.total_inc_dec(2),
            100,
            "Testing 10^100 inc_dec numbers."
        )

        self.assertEqual(
            Numtools.total_inc_dec(100),
            51161058134251,
            "Testing 10^100 inc_dec numbers."
        )

    def test_joins(self):
        # m1 = [['+', '-']]
        # m2 = [['1', '2', '3'], ['4', '5', '6']]
        # m3 = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]
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
        self.assertEqual(
            Sorts.counting_sort([1, 3, 2, 4, 6, 5, 2, 7]), [1, 2, 2, 3, 4, 5, 6, 7],
            "Testing counting sort"
        )
        self.assertEqual(
            Sorts.counting_sort([7, 6, 5, 4, 3, 2], 7), [2, 3, 4, 5, 6, 7],
            "Testing counting sort"
        )
        self.assertEqual(
            Sorts.counting_sort([1, 1, 1, 1, 1, 1], 2), [1, 1, 1, 1, 1, 1],
            "Testing counting sort"
        )
        self.assertEqual(
            Sorts.heap_sort([1, 3, 2, 4, 6, 5, 2, 7]), [1, 2, 2, 3, 4, 5, 6, 7],
            "Testing heap sort"
        )
        self.assertEqual(
            Sorts.heap_sort([7, 6, 5, 4, 3, 2]), [2, 3, 4, 5, 6, 7],
            "Testing heap sort"
        )
        self.assertEqual(
            Sorts.heap_sort([1, 1, 1, 1, 1, 1]), [1, 1, 1, 1, 1, 1],
            "Testing heap sort"
        )
        self.assertTrue(
            Sorts.is_sorted([1, 1, 1, 1, 1, 1]),
            "Testing if list is sorted ASC"
        )
        self.assertTrue(
            Sorts.is_sorted([1, 2, 3, 4, 5, 6]),
            "Testing if list is sorted ASC"
        )
        self.assertTrue(
            Sorts.is_sorted([1, 2, 3, 4, 5, 6], order="ASC"),
            "Testing if list is sorted ASC"
        )
        self.assertTrue(
            Sorts.is_sorted([1, 1, 1, 1, 1, 1], order="DESC"),
            "Testing if list is sorted DESC"
        )
        self.assertTrue(
            Sorts.is_sorted([6, 5, 4, 3, 2, 1], order="DESC"),
            "Testing if list is sorted DESC"
        )
        self.assertFalse(
            Sorts.is_sorted([4, 2, 1, 5, 6, 7], order="ASC"),
            "Testing if list is not sorted ASC"
        )
        self.assertFalse(
            Sorts.is_sorted([4, 2, 1, 5, 6, 7], order="DESC"),
            "Testing if list is not sorted DESC"
        )
        self.assertFalse(
            Sorts.is_sorted([6, 5, 4, 3, 2, 1], order="ASC"),
            "Testing if list is not sorted ASC"
        )
        self.assertFalse(
            Sorts.is_sorted([1, 2, 3, 4, 5, 6], order="DESC"),
            "Testing if list is not sorted DESC"
        )

    def test_math(self):
        self.assertEqual(
            Math.partial_permutation(21, 7),
            586051200,
            "Testing partial permutation"
        )
        self.assertEqual(
            Math.binomial_coefficient(21, 7),
            116280,
            "Testing binomial coefficient"
        )
        self.assertEqual(
            Math.sum_arithmetic_series(10),
            55,
            "Testing sum_arithmetic_series(10)"
        )
        self.assertEqual(
            Math.sum_arithmetic_series(50),
            sum(i for i in range(51)),
            "Testing sum_arithmetic_series(51)"
        )
        self.assertEqual(
            Math.sum_arithmetic_series(50, a = 10),
            sum(i for i in range(10, 51)),
            "Testing sum_arithmetic_series(51, a = 10)"
        )
        self.assertEqual(
            Math.sum_arithmetic_series(1),
            1,
            "Testing sum_arithmetic_series(1)"
        )
        self.assertEqual(
            Math.sum_arithmetic_series(0),
            0,
            "Testing sum_arithmetic_series(0)"
        )
        self.assertEqual(
            Math.sum_square_series(5),
            55,
            "Testing sum_square_series(5)"
        )
        self.assertEqual(
            Math.sum_square_series(1),
            1,
            "Testing sum_square_series(1)"
        )
        self.assertEqual(
            Math.sum_square_series(0),
            0,
            "Testing sum_square_series(0)"
        )
        self.assertEqual(
            Math.sum_square_series(100),
            sum(i**2 for i in range(101)),
            "Testing sum_square_series(100)"
        )
        self.assertEqual(
            Math.sum_square_series(100, a = 25),
            sum(i**2 for i in range(25, 101)),
            "Testing sum_square_series(100, a = 25)"
        )
        self.assertEqual(
            Math.sum_cubic_series(4),
            100,
            "Testing sum_cubic_series(4)"
        )
        self.assertEqual(
            Math.sum_cubic_series(1),
            1,
            "Testing sum_cubic_series(1)"
        )
        self.assertEqual(
            Math.sum_cubic_series(0),
            0,
            "Testing sum_cubic_series(0)"
        )
        self.assertEqual(
            Math.sum_cubic_series(100),
            sum(i**3 for i in range(101)),
            "Testing sum_cubic_series(100)"
        )
        self.assertEqual(
            Math.sum_cubic_series(100, a = 25),
            sum(i**3 for i in range(25, 101)),
            "Testing sum_cubic_series(100, a = 25)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(4),
            20,
            "Testing sum_tetrahedral_series(4)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(1),
            1,
            "Testing sum_tetrahedral_series(1)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(0),
            0,
            "Testing sum tetrahedral_series(0)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(10),
            220,
            "Testing sum_tetrahedral_series(10)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(4, a = 2),
            19,
            "Testing sum_tetrahedral_series(4, a = 2)"
        )
        self.assertEqual(
            Math.sum_tetrahedral_series(5, a = 3),
            31,
            "Testing sum_tetrahedral_series(5, a = 3)"
        )
        self.assertEqual(
            Math.manhattan_distance((1, 1), (2, 4)),
            4,
            "Testing manhattan_distance((1, 1), (2, 4))"
        )
        self.assertEqual(
            Math.manhattan_distance((0, 0), (0, 0)),
            0,
            "Testing manhattan_distance((0, 0), (0, 0))"
        )
        self.assertEqual(
            Math.manhattan_distance((1, 2, 3, 4), (5, 6, 7, 8)),
            16,
            "Testing manhattan_distance((1, 2, 3, 4), (5, 6, 7, 8))"
        )
        self.assertEqual(
            Math.manhattan_distance((0, 0, 0, 0), (0, 0, 0, 0)),
            0,
            "Testing manhattan_distance((0, 0, 0, 0), (0, 0, 0, 0))"
        )
        self.assertEqual(
            Math.euclidean_distance((1, 2, 3, 4), (5, 6, 7, 8)),
            8,
            "Testing euclidean_distance((1, 2, 3, 4), (5, 6, 7, 8))"
        )
        self.assertEqual(
            Math.euclidean_distance((0, 0, 0, 0), (0, 0, 0, 0)),
            0,
            "Testing euclidean_distance((0, 0, 0, 0), (0, 0, 0, 0))"
        )

    def test_algs(self):
        self.assertEqual(
            Algorithms.jaccard_index({"A"}, {"B"}),
            0,
            "Testing jaccard_index({A}, {B})"
        )
        self.assertEqual(
            Algorithms.jaccard_index({"A", "B"}, {"B"}),
            0.5,
            "Testing jaccard_index({A, B}, {B})"
        )
        self.assertEqual(
            Algorithms.jaccard_index({"A", "B", "C"}, {"B", "C", "A"}),
            1,
            "Testing jaccard_index({A, B, C}, {B, C, A})"
        )
        self.assertEqual(
            Algorithms.jaccard_distance({"A"}, {"A"}),
            0,
        )
        self.assertEqual(
            Algorithms.jaccard_distance({"A", "B", "C", "D"}, {"A"}),
            0.75,
            "Testing jaccard_distance({A, B, C, D}, {A})"
        )
        self.assertEqual(
            Algorithms.levenshtein_distance("ABCD", "BCDE"),
            2,
            "Testing levenshtein_distance(ABCD, BCDE)"
        )
        self.assertEqual(
            Algorithms.levenshtein_distance("ABCD", ""),
            4,
            "Testing levenshtein_distance(ABCD, )"
        )
        self.assertEqual(
            Algorithms.levenshtein_distance("", "ABCDE"),
            5,
            "Testing levenshtein_distance(, ABCDE)"
        )
        self.assertEqual(
            Algorithms.levenshtein_distance("", ""),
            0,
            "Testing levenshtein_distance(, )"
        )
        self.assertEqual(
            Algorithms.substring_counter("", ""),
            1,
            "Testing substring_counter(, )"
        )
        self.assertEqual(
            Algorithms.substring_counter("A", ""),
            0,
            "Testing substring_counter(A, )"
        )
        self.assertEqual(
            Algorithms.substring_counter("", "A"),
            -1,
            "Testing substring_counter(, A)"
        )
        self.assertEqual(
            Algorithms.substring_counter("AAAA", "AA"),
            3,
            "Testing substring_counter(AAAA, AA)"
        )
        self.assertEqual(
            Algorithms.substring_counter("CCCAACACC", "CC"),
            3,
            "Testing substring_counter(CCCAACACC, CC)"
        )

if __name__ == "__main__":
    tests = Tests()

    print("Testing Primes")
    tests.test_primes()

    print("Testing Numtools")
    tests.test_nums()

    print("Testing Joins")
    tests.test_joins()

    print("Testing Sorts")
    tests.test_sorts()

    print("Testing Math")
    tests.test_math()

    print("Testing Algorithms")
    tests.test_algs()
