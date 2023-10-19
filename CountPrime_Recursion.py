def is_prime(num, divisor=2):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    if divisor * divisor > num:
        return True
    if num % divisor == 0:
        return False

    return is_prime(num, divisor + 1)

def count_prime_recursive(num):
    if num <= 1:
        return 0
    if is_prime(num):
        return 1 + count_prime_recursive(num - 1)
    else:
        return count_prime_recursive(num - 1)

count = count_prime_recursive(13)
print(count)
