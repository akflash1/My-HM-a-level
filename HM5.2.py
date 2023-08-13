def square(x):
    return x ** 2

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = list(range(51))
squared_primes = map(square, filter(is_prime, numbers))
print(list(squared_primes))
