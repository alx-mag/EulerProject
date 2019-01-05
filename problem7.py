def is_prime(_number):
    for x in range(2, _number):
        if _number % x == 0:
            return False

    return True


def next_prime(prime):
    next = prime + 1
    while not is_prime(next):
        next += 1
    return next


if __name__ == '__main__':
    count = 1
    prime_number = 1
    while count < 10002:
        count += 1
        prime_number = next_prime(prime_number)
        print("# %d: %d" % (count, prime_number))
    print("Found prime: " + str(prime_number))
