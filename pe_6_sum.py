"""
NicksPizza
Project Euler .net

Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
...
The square of the sum of the first ten natural numbers is,
...
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

Answer: 25164150
"""


def sum_of_the_squares(n):
    return n * (n+1) * (2*n+1) // 6


def squares_of_the_sum(n):
    results = n * (n+1) // 2
    return results ** 2


