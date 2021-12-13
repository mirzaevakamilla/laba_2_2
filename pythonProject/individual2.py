#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

if __name__ == '__main__':
    a = int(input("Value of a? "))
    b = int(input("Value of b? "))
    c = int(input("Value of c? "))

    d = b**2 - 4 * a * c
    if d > 0:
        print(f"x1 = {((-b) + math.sqrt(d)) / 2 * a} x2 = {((-b) - math.sqrt(d)) / 2 * a}")
    elif d == 0:
        print(f"x = {(-b)} / {2 * a}")
    else:
        print(f"x1 = ({-b} + i * math.sqrt({d})) / {2 * a} \n x1 = ({-b} - i * math.sqrt({d})) / {2 * a}")
