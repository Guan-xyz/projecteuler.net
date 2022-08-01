"""
NicksPizza
Project Euler .net

Multiples of 3 or 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""


# 1
def euler_one(m, upper_limit):
    sums = 0
    for x in range(1, upper_limit+1):
        if x % m == 0:
            sums += x
    return sums


# 2
def euler_one_(m, upper_limit):
    p = upper_limit // m
    return m*p*(p+1) // 2
