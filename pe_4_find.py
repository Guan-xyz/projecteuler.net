"""
NicksPizza
Project Euler .net

Largest palindrome product
Problem 4

A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""


def reverse(n):
    reverses = 0
    while n > 0:
        reverses = 10 * reverses + n % 10
        n = n // 10
    return reverses


def is_palindrome(n):
    return n == reverse(n)


def euler_four(n):
    a = n
    largest_palindrome = 0
    while a >= 100:
        b = n
        while b >= a:
            if a * b <= largest_palindrome:
                break
            if is_palindrome(a * b):
                largest_palindrome = a * b
            b = b - 1
        a = a - 1
    return largest_palindrome
