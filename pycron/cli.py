import argparse
import re

MINUTE_REGEX = "[0-5]?[0-9]"
HOUR_REGEX = "(2[0-3]|1[0-9]|[0-9])"
DAY_OF_MONTH_REGEX = "(3[01]|[12][0-9]|[1-9])"
MONTH_REGEX = "(1[0-2]|[1-9])"


class Validate:
    def __init__(self, exp: str, imax: int, imin: int = 1):
        self.exp = exp
        self.imin = imin
        self.imax = imax

    def __call__(self, value: str):
        if value == "*":
            return [n for n in range(self.imin, self.imax)]

        if re.match(f"^{self.exp}$", value):
            return [int(value)]

        if re.match(f"^\*\/{self.exp}$", value):
            number = int(value[2:])
            response = [n for n in range(0, self.imax, number)]

            if self.imin > 0:
                return response[1:]

            return response

        if re.match(f"^{self.exp}(,{self.exp})*$", value):
            return [int(n) for n in value.split(",")]

        if re.match(f"^{self.exp}(-{self.exp})$", value):
            start, end = [int(n) for n in value.split("-")]
            return [n for n in range(start, end + 1)]

        raise argparse.ArgumentTypeError(f"Invalid expression: {value}")


def show(msg: str, numbers: list[int]):
    print("{0:14}{1}".format(msg, " ".join([str(n) for n in numbers])))


def main(args):
    show("minute", args.minutes)
    show("hour", args.hours)
    show("day of month", args.day_of_month)
    show("month", args.month)
    print("{0:14}{1}".format("command", " ".join(args.command)))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PyCron - Cronjob make in Python")
    parser.add_argument(
        "minutes", type=Validate(MINUTE_REGEX, imax=60, imin=0), help="Help message"
    )
    parser.add_argument(
        "hours", type=Validate(HOUR_REGEX, imax=24, imin=0), help="Help message"
    )
    parser.add_argument(
        "day_of_month",
        type=Validate(DAY_OF_MONTH_REGEX, imax=32),
        help="Help message",
    )
    parser.add_argument(
        "month", type=Validate(MONTH_REGEX, imax=13), help="Help message"
    )
    parser.add_argument("command", type=str, nargs="*", help="Help message")

    args = parser.parse_args()

    main(args)

"""
Minutes
    - [0-59]
    - *
    - */[0-59]
    - 1,2
    - 1-5
"""
