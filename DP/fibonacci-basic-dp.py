"""
Basic DP implementation
"""


def fibonacci(n, cache={}):
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    else:
        result = fibonacci(n-1) + fibonacci(n-2)
    cache[n] = result
    return result


print(fibonacci(999))
