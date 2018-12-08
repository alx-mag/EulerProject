def is_the_number(number):
    for x in range(1, 21):
        if number % x != 0:
            return False
    return True


def resolve():
    koeff = 1
    base = 20
    while True:
        test_num = koeff * base
        if is_the_number(test_num):
            return test_num
        koeff += 1


if __name__ == '__main__':
    print(resolve())
