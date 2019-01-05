def is_prime(number):
    if number == 1 | number == 2:
        return True

    factor = 2
    while factor < number:
        if number % factor == 0:
            return False
        factor += 1

    return True


def get_next_prime(after_number):
    next_number = after_number + 1
    while not is_prime(next_number):
        next_number += 1
    return next_number


def find_prime_factor(number):
    prime_factors = []
    _factor = 2
    while _factor < number:
        if is_prime(_factor):
            if number % _factor == 0:
                prime_factors.append(_factor)
                number = number / _factor
        _factor += 1
    return prime_factors


if __name__ == '__main__':
    print(is_prime())

