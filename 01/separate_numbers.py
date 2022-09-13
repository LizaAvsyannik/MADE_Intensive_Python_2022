def separate(lst):
    even_lst = [el for el in lst if el % 2 == 0]
    odd_lst = [el for el in lst if el % 2 != 0]
    return even_lst, odd_lst


if __name__ == "__main__":
    lst = range(20)
    separated_lists = separate(lst)
    assert separated_lists == (list(range(0, 20, 2)), list(range(1, 20, 2)))

    lst = [3, 5, 2, 4, 6, 7, 8, 9, 0]
    separated_lists = separate(lst)
    assert separated_lists == ([2, 4, 6, 8, 0], [3, 5, 7, 9])

    print('Tests initial list has both even and odd numbers - OK')

    lst = range(0, 20, 2)
    separated_lists = separate(lst)
    assert separated_lists == (list(range(0, 20, 2)), [])
    print('Test initial list has only even numbers - OK')

    lst = range(1, 20, 2)
    separated_lists = separate(lst)
    assert separated_lists == ([], list(range(1, 20, 2)))
    print('Test initial list has only odd numbers - OK')
