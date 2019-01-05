ADJACENT_DIGITS_NUMBER = 13


def product(list):
    result = 1
    for x in list:
        result *= x
    return result


def init_list():
    file = open("resources/problem8.txt", "r")
    content = file.read().replace("\n", "")

    result_list = []
    for c in content:
        result_list.append(int(c))

    return result_list


def resolve():
    main_list = init_list()
    print(f'Full main_list: {main_list}')
    max_product = -1
    max_product_list = []
    indices_range = range(0, main_list.__len__() - ADJACENT_DIGITS_NUMBER + 1)
    for i in indices_range:
        sublist = main_list[i:i+ADJACENT_DIGITS_NUMBER]
        sublist_product = product(sublist)
        print(f'{sublist} = {sublist_product}')

        if sublist_product > max_product:
            max_product = sublist_product
            max_product_list = sublist

    print(f'Max product: {max_product} of main_list {max_product_list}')


if __name__ == '__main__':
    resolve()
