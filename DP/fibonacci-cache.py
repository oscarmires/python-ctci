"""
Bottom-up implementation, pythonic

Taken from 'Elements of programming interviews in Python'
"""


def fibonacci(n, cache={}):
    if n <= 1:
        return n
    if n not in cache:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]


print(fibonacci(998))
