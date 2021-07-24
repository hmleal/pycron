# Pycron

> The quick and simple editor for cron schedule expressions

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Requirements

* Python (3.9)

There's no extra dependencies

## 🏃🏻 Running

    python pycron cli.py --help
    python pycron cli.py "*/15 0 1,15 * 1-5 /usr/bin/find"

Every paramenter accepts the following expressions

    n -> Any valid integer (example for month the range is 1-12)
    * -> Every possibility (example for month result it will be 1,2,3,4,5,6,7,8,9,10,11,12)
    */n -> Every x days/minutes after the begning
    1,2 -> Selection of days/minutes
    1-5 -> Sequence of days/minutes (start-end)

## ⚙️ Testing

Just run the following command from your terminal

    python -m unittest
