"""
NicksPizza
Project Euler .net

Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Answer:
"""


def gcd(x, y):
    if y > 0:
        return gcd(y, x % y)
    else:
        return x


def lcm(x, y):
    return x * y // gcd(x, y)


a_boy = 1
for b_boy in range(2, 21):
    a_boy = lcm(a_boy, b_boy)
print(a_boy)
