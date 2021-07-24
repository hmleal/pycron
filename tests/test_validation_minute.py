import argparse
import unittest

from pycron.cli import (
    day_of_month_validation,
    hour_validation,
    minute_validation,
    month_validation,
)


class TestMinuteValidation(unittest.TestCase):
    def test_any_parser(self):
        expected = [n for n in range(0, 60)]

        self.assertListEqual(expected, minute_validation("*"))

    def test_range_integer_validation(self):
        for n in range(0, 60):
            self.assertListEqual([n], minute_validation(str(n)))

    def test_every_x_time_parser(self):
        self.assertListEqual([0, 15, 30, 45], minute_validation("*/15"))
        self.assertListEqual([0, 10, 20, 30, 40, 50], minute_validation("*/10"))

    def test_list_of_integers_parser(self):
        self.assertListEqual([1, 2], minute_validation("1,2"))
        self.assertListEqual([15, 23], minute_validation("15,23"))

    def test_validation_error_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            minute_validation("60")

        with self.assertRaises(argparse.ArgumentTypeError):
            minute_validation("*/60")

        with self.assertRaises(argparse.ArgumentTypeError):
            minute_validation("1,60")

        with self.assertRaises(argparse.ArgumentTypeError):
            minute_validation("1-60")


class TestHourValidation(unittest.TestCase):
    def test_any_parser(self):
        expected = [n for n in range(0, 24)]

        self.assertListEqual(expected, hour_validation("*"))

    def test_range_integer_validation(self):
        for n in range(0, 24):
            self.assertListEqual([n], hour_validation(str(n)))

    def test_every_x_time_parser(self):
        self.assertListEqual([0, 4, 8, 12, 16, 20], hour_validation("*/4"))
        self.assertListEqual([0, 8, 16], hour_validation("*/8"))

    def test_list_of_integers_parser(self):
        self.assertListEqual([1, 2], hour_validation("1,2"))
        self.assertListEqual([15, 23], hour_validation("15,23"))

    def test_validation_error_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            hour_validation("24")

        with self.assertRaises(argparse.ArgumentTypeError):
            hour_validation("*/24")

        with self.assertRaises(argparse.ArgumentTypeError):
            hour_validation("1,24")

        with self.assertRaises(argparse.ArgumentTypeError):
            hour_validation("1-24")


class TestDayOfMonthValidation(unittest.TestCase):
    def test_any_parser(self):
        expected = [n for n in range(1, 32)]

        self.assertListEqual(expected, day_of_month_validation("*"))

    def test_range_integer_validation(self):
        for n in range(1, 32):
            self.assertListEqual([n], day_of_month_validation(str(n)))

    def test_every_x_time_parser(self):
        self.assertListEqual(
            [0, 4, 8, 12, 16, 20, 24, 28], day_of_month_validation("*/4")
        )
        self.assertListEqual([0, 8, 16, 24], day_of_month_validation("*/8"))

    def test_list_of_integers_parser(self):
        self.assertListEqual([1, 2], day_of_month_validation("1,2"))
        self.assertListEqual([15, 23], day_of_month_validation("15,23"))

    def test_validation_error_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            day_of_month_validation("0")

        with self.assertRaises(argparse.ArgumentTypeError):
            day_of_month_validation("32")

        with self.assertRaises(argparse.ArgumentTypeError):
            day_of_month_validation("*/32")

        with self.assertRaises(argparse.ArgumentTypeError):
            day_of_month_validation("1,32")

        with self.assertRaises(argparse.ArgumentTypeError):
            day_of_month_validation("1-32")


class TestMonthValidation(unittest.TestCase):
    def test_any_parser(self):
        expected = [n for n in range(1, 13)]

        self.assertListEqual(expected, month_validation("*"))

    def test_range_integer_validation(self):
        for n in range(1, 13):
            self.assertListEqual([n], month_validation(str(n)))

    def test_every_x_time_parser(self):
        self.assertListEqual([0, 4, 8, 12], month_validation("*/4"))
        self.assertListEqual([0, 8], month_validation("*/8"))

    def test_list_of_integers_parser(self):
        self.assertListEqual([1, 2], month_validation("1,2"))
        self.assertListEqual([7, 9], month_validation("7,9"))

    def test_validation_error_should_raise_error(self):
        with self.assertRaises(argparse.ArgumentTypeError):
            month_validation("0")

        with self.assertRaises(argparse.ArgumentTypeError):
            month_validation("13")

        with self.assertRaises(argparse.ArgumentTypeError):
            month_validation("*/13")

        with self.assertRaises(argparse.ArgumentTypeError):
            month_validation("1,13")

        with self.assertRaises(argparse.ArgumentTypeError):
            month_validation("1-13")
