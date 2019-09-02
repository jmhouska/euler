from math import sqrt

def is_prime(n):
    if n in (2, 3, 5, 7, 11):  # special case small primes
        return True
    if n % 2 == 0 or n == 1:  # special case even numbers and 1
        return False
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    max_value = 600851475143
    current_value = 2
    outputs = []
    while current_value < max_value:
        if is_prime(current_value) and (max_value / current_value).is_integer():
            outputs.append(current_value)
            max_value = max_value / current_value
        else:
            current_value = current_value + 1
    if is_prime(max_value):
        outputs.append(int(max_value))
    print(outputs)