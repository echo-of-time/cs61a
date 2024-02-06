"""Our first Python source file"""

from operator import floordiv, mod

def divide_exact(n, d=10):
    """Return the quotient and remainder of dividing N by D
    
    >>> q, r = divide_exact(2024, 10)
    >>> q
    202
    >>> r
    4
    """
    return floordiv(n, d), mod(n, d)

def absolute_value(x):
    """Return the absolute value of x."""
    if x < 0:
        return -x
    else:
        return x

def prime_factors(n):
    """Print the prime factors of n in non-decreasing order.
    >>> prime_factors(8)
    2
    2
    2
    >>> prime_factors(9)
    3
    3
    >>> prime_factors(10)
    2
    5
    >>> prime_factors(11)
    11
    >>> primr_factors(12)
    2
    2
    3
    >>> prime_factors(858)
    2
    3
    11
    12
    """
    while n > 1:
        k = smallest_prime_factor(n)
        n = n // k
        print(k)

def smallest_prime_factor(n):
    """Retrurn the smallest k > 1 that evenly divides n."""
    k = 2
    while n % k != 0:
        k = k + 1
    return k


