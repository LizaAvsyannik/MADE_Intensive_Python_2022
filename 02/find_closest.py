from collections import defaultdict


def find_closest_to_zero(lst):
    abs_dict = defaultdict(list)
    for elem in lst:
        abs_dict[abs(elem)].append(elem)
    return min(abs_dict.items(), key=lambda elem: elem[0])[1]


if __name__ == "__main__":
    lst = [-5, 9, 6, -8] 
    res = find_closest_to_zero(lst)
    assert res == [-5]
    print('Test1 - OK')

    lst = [-1, 2, -5, 1, -1]
    res = find_closest_to_zero(lst)
    assert res == [-1, 1, -1]
    print('Test2 - OK')

    lst = [-1, 2, -5, 1, 0]
    res = find_closest_to_zero(lst)
    assert res == [0]
    print('Test3 - OK')

    lst = [-2, 2, -5, 2, -2, 2, 6, 8]
    res = find_closest_to_zero(lst)
    assert res == [-2, 2, 2, -2, 2]
    print('Test4 - OK')
    