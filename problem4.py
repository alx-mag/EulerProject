def is_palindrome(number):
    return str(number)[::-1] == str(number)


def resolve():
    answer_vars = [-1, -1, -1]
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, 1000)):
            mult = x * y
            if is_palindrome(mult) and mult > answer_vars[2]:
                answer_vars = [x, y, mult]

    return "Found %d * %d == %d" % (answer_vars[0], answer_vars[1], answer_vars[2])


if __name__ == '__main__':
    print(resolve())
