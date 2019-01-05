def sum_of_squares(count):
    _sum = 0
    for x in range(1, count + 1):
        _sum += pow(x, 2)
    return _sum


def square_of_sum(count):
    _sum = 0
    for x in range(1, count + 1):
        _sum += x
    return pow(_sum, 2)


if __name__ == '__main__':
    count = 100
    print("The difference: " + str(abs(sum_of_squares(count) - square_of_sum(count))))
