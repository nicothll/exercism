def primes(limit: int) -> list[int]:
    """
     Generate a list of prime numbers up to the given limit using Sieve of Eratosthenes algorithm.

    Args:
        limit: The upper bound of the range to generate prime numbers.

    Returns:
        A list of prime numbers from 2 to the limit, inclusive.

    Examples:
        >> primes(10)
        [2, 3, 5, 7]
        >> primes(20)
        [2, 3, 5, 7, 11, 13, 17, 19]

    Raises:
        TypeError: If the input limit is not an integer.
        ValueError: If the input limit is less than 2.
    """
    numbers = range(limit + 1)
    prime = [True for _ in numbers]

    p = 2
    while p * p < limit:
        if prime[p] == True:
            for i in range(p * p, limit + 1, p):
                # Updates the multiples of p
                prime[i] = False
        p += 1
    return list(filter(lambda x: prime[x], numbers))[2:]
