#!/usr/bin/env python
# coding=utf-8

import pendulum


class DateTime:
    @staticmethod
    def today():
        return pendulum.today()

    @staticmethod
    def now():
        return pendulum.now()


if __name__ == "__main__":
    print(DateTime.today())
    print(DateTime.now())
