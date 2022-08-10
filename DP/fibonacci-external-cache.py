"""
Bottom-up implementation with cache, non-pythonic
"""


def fibonacci(n, cache):
    if n < 2:
        return n
    if n not in cache:
        cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]


sample_cache = {}
print(fibonacci(998, sample_cache))
