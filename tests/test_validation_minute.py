import argparse
import unittest
from pycron.cli import Validate


class TestMinuteValidation(unittest.TestCase):
    def setUp(self):
        self.validation = Validate("[0-5]?[0-9]", imax=60, imin=0)

    def test_asterisk_validation(self):
        expected = [n for n in range(0, 60)]
        self.assertListEqual(expected, self.validation("*"))

    def test_number_validation(self):
        self.assertListEqual([0], self.validation("0"))
        self.assertListEqual([23], self.validation("23"))
        self.assertListEqual([59], self.validation("59"))

    def test_division_validation(self):
        self.assertListEqual([0, 15, 30, 45], self.validation("*/15"))
        self.assertListEqual([0, 10, 20, 30, 40, 50], self.validation("*/10"))

    def test_list_validation(self):
        self.assertListEqual([1, 2], self.validation("1,2"))
        self.assertListEqual([1, 15], self.validation("1,15"))

    def test_sequence_validation(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.validation("1-5"))
        self.assertListEqual([17, 18, 19, 20, 21, 22, 23], self.validation("17-23"))

    def test_validation_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("60")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("*/60")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1,60")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1-60")


class TestHourValidation(unittest.TestCase):
    def setUp(self):
        self.validation = Validate("(2[0-3]|1[0-9]|[0-9])", imax=24, imin=0)

    def test_asterisk_validation(self):
        expected = [n for n in range(0, 24)]
        self.assertListEqual(expected, self.validation("*"))

    def test_number_validation(self):
        self.assertListEqual([0], self.validation("0"))
        self.assertListEqual([13], self.validation("13"))
        self.assertListEqual([23], self.validation("23"))

    def test_division_validation(self):
        self.assertListEqual([0, 4, 8, 12, 16, 20], self.validation("*/4"))
        self.assertListEqual([0, 8, 16], self.validation("*/8"))

    def test_list_validation(self):
        self.assertListEqual([1, 11, 8], self.validation("1,11,8"))
        self.assertListEqual([1, 21, 23], self.validation("1,21,23"))

    def test_sequence_validation(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.validation("1-5"))
        self.assertListEqual([17, 18, 19, 20, 21, 22, 23], self.validation("17-23"))

    def test_validation_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("24")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("*/24")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1,3,24")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1-60")


class TestDayOfMonthValidation(unittest.TestCase):
    def setUp(self):
        self.validation = Validate("(3[01]|[12][0-9]|[1-9])", imax=32)

    def test_asterisk_validation(self):
        expected = [n for n in range(1, 32)]
        self.assertListEqual(expected, self.validation("*"))

    def test_number_validation(self):
        self.assertListEqual([1], self.validation("1"))
        self.assertListEqual([13], self.validation("13"))
        self.assertListEqual([23], self.validation("23"))

    def test_division_validation(self):
        self.assertListEqual([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], self.validation("*/3"))
        self.assertListEqual([8, 16, 24], self.validation("*/8"))

    def test_list_validation(self):
        self.assertListEqual([1, 11, 8], self.validation("1,11,8"))
        self.assertListEqual([1, 21, 23], self.validation("1,21,23"))

    def test_sequence_validation(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.validation("1-5"))
        self.assertListEqual([17, 18, 19, 20, 21, 22, 23], self.validation("17-23"))

    def test_validation_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("0")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("*/32")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1,3,32")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1-32")


class TestMonthValidation(unittest.TestCase):
    def setUp(self):
        self.validation = Validate("(1[0-2]|[1-9])", imax=13)

    def test_asterisk_validation(self):
        expected = [n for n in range(1, 13)]
        self.assertListEqual(expected, self.validation("*"))

    def test_number_validation(self):
        self.assertListEqual([1], self.validation("1"))
        self.assertListEqual([7], self.validation("7"))
        self.assertListEqual([12], self.validation("12"))

    def test_division_validation(self):
        self.assertListEqual([1,2,3,4,5,6,7,8,9,10,11,12], self.validation("*/1"))
        self.assertListEqual([8], self.validation("*/8"))
        self.assertListEqual([3, 6, 9, 12], self.validation("*/3"))

    def test_list_validation(self):
        self.assertListEqual([1, 7, 9], self.validation("1,7,9"))
        self.assertListEqual([1, 7, 12], self.validation("1,7,12"))

    def test_sequence_validation(self):
        self.assertListEqual([1, 2, 3, 4, 5], self.validation("1-5"))
        self.assertListEqual([9, 10, 11, 12], self.validation("9-12"))

    def test_validation_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("0")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("*/32")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1,3,32")

        with self.assertRaises(argparse.ArgumentTypeError):
            self.validation("1-32")