def fibonacci(n):
    """
    Recursive function to compute the nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)


# Test cases
print(fibonacci(0))   # Expected output: 0
print(fibonacci(1))   # Expected output: 1
print(fibonacci(2))   # Expected output: 1
print(fibonacci(3))   # Expected output: 2
print(fibonacci(5))   # Expected output: 5
print(fibonacci(7))   # Expected output: 13
print(fibonacci(10))  # Expected output: 55