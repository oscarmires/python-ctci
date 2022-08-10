def fibonacci(n):
    if n < 2:
        return n

    fib_minus_2, fib_minus_1 = 0, 1

    for _ in range(1, n):
        f = fib_minus_2 + fib_minus_1
        fib_minus_2, fib_minus_1 = fib_minus_1, f
    return fib_minus_1


print(fibonacci(100000))
