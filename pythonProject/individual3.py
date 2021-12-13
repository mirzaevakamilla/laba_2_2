#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    n = int(input("Введите значение n: "))
    k = int(input("Введите значение k: "))

    s = 0
    if n == 1:
        for n in range(1, 10, 1):
            if n % k == 0:
                s = s + n
    if n == 2:
        for n in range(10, 100, 1):
            if n % k == 0:
                s = s + n
    if n == 3:
        for n in range(100, 1000, 1):
            if n % k == 0:
                s = s + n
    if n == 4:
        for n in range(1000, 10000, 1):
            if n % k == 0:
                s += n
print(f"Сумма равна = {s}")
