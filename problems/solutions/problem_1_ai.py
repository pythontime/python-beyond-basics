limit = 100_000

# Sieve of Eratosthenes
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for multiple in range(i * i, limit, i):
            is_prime[multiple] = False

prime_sum = sum(i for i, prime in enumerate(is_prime) if prime)

print(prime_sum)


# ----------------------------------------------------
# That's a little complicated for me.
# Can you rewrite for a junior developer to understand?
# Follow the zen of Python

def is_prime(number: int) -> bool:
    """Return True if number is prime, otherwise False."""
    if number < 2:
        return False

    # Only need to try dividing up to the square root of the number
    limit = int(number ** 0.5) + 1
    for divisor in range(2, limit):
        if number % divisor == 0:
            return False

    return True


def sum_primes_below(limit: int) -> int:
    """Return the sum of all prime numbers below 'limit'."""
    total = 0
    for n in range(2, limit):
        if is_prime(n):
            total += n
    return total


if __name__ == "__main__":
    limit = 100_000
    result = sum_primes_below(limit)
    print(f"Sum of primes below {limit}: {result}")