def factorial(n):
    """
    Recursive function to calculate the factorial of a non-negative integer.
    """
    # Base case
    if n == 0:
        return 1

    # Recursive case
    return n * factorial(n - 1)


# Test cases
print(factorial(0))  # Expected output: 1
print(factorial(1))  # Expected output: 1
print(factorial(3))  # Expected output: 6
print(factorial(5))  # Expected output: 120
print(factorial(7))  # Expected output: 5040