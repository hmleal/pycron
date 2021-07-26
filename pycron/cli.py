import argparse
import re

MINUTE_REGEX = "[0-5]?[0-9]"
HOUR_REGEX = "(2[0-3]|1[0-9]|[0-9])"
DAY_OF_MONTH_REGEX = "(3[01]|[12][0-9]|[1-9])"
MONTH_REGEX = "(1[0-2]|[1-9])"
DAY_OF_WEEK_REGEX = "[0-6]"


def _base_validation(exp: str, value: str, end: int, start: int = 0):
    if value == "*":
        return [n for n in range(start, end)]

    if re.match(f"^{exp}$", value):
        return [int(value)]

    if re.match(f"^\*\/{exp}$", value):
        number = int(value[2:])
        response = [n for n in range(0, end, number)]

        return response

    if re.match(f"^{exp}(,{exp})*$", value):
        return [int(n) for n in value.split(",")]

    if re.match(f"^{exp}(-{exp})$", value):
        imin, imax = [int(n) for n in value.split("-")]
        return [n for n in range(imin, imax + 1)]

    raise argparse.ArgumentTypeError(f"Invalid expression: {value}")


def minute_validation(value: str):
    return _base_validation(exp=MINUTE_REGEX, start=0, end=60, value=value)


def hour_validation(value: str):
    return _base_validation(exp=HOUR_REGEX, start=0, end=24, value=value)


def day_of_month_validation(value: str):
    return _base_validation(exp=DAY_OF_MONTH_REGEX, start=1, end=32, value=value)


def month_validation(value: str):
    return _base_validation(exp=MONTH_REGEX, start=1, end=13, value=value)


def day_of_week_validation(value: str):
    return _base_validation(exp=DAY_OF_MONTH_REGEX, start=0, end=7, value=value)


def command_validation(value: str):
    # TODO Just in need some extra validation here
    return value


def validate_cron_string(value):
    args = value.split(" ", maxsplit=5)

    validators = [
        minute_validation,
        hour_validation,
        day_of_month_validation,
        month_validation,
        day_of_week_validation,
        command_validation,
    ]

    if len(args) != 6:
        raise argparse.ArgumentTypeError(f"Invalid string: `{value}`")

    return [func(arg) for arg, func in zip(args, validators)]


def show(args: list[int]):
    arg_names = ["minute", "hour", "day of month", "month", "day of week", "command"]

    for name, values in zip(arg_names, args):
        if name != "command":
            print("{0:14}{1}".format(name, " ".join([str(n) for n in values])))
        else:
            print("{0:14}{1}".format(name, values))


def main():
    parser = argparse.ArgumentParser(description="PyCron - Cronjob make in Python")
    parser.add_argument("cron_string", type=validate_cron_string, help="Help message")

    args = parser.parse_args()

    show(args.cron_string)


if __name__ == "__main__":
    main()

"""
Minutes
    - [0-59]
    - *
    - */[0-59]
    - 1,2
    - 1-5
"""
