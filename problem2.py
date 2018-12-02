def init_fib_sequence(max_value):
    seq = [1, 2]

    while True:
        next_num = create_next_num(seq)
        if next_num < max_value:
            seq.append(next_num)
        else:
            break

    return seq


def create_next_num(seq):
    return seq[-1] + seq[-2]


def calc_even_sum(_list):
    even_sum = 0
    for element in _list:
        if element % 2 == 0:
            even_sum += element
    return even_sum


if __name__ == '__main__':
    sequence = init_fib_sequence(4_000_000)
    _sum = calc_even_sum(sequence)
    print(_sum)
