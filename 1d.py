# 1.5) Calculates the nth Fibonacci number using a function.
def fibonacci_number(n):
    """Calculates the nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b



n_fib = 10
result = fibonacci_number(n_fib)
print(f"The {n_fib}th Fibonacci number is: {result}")
