def merge(lst1, lst2):
    return sorted(list(set(lst1).intersection(set(lst2))))


if __name__ == "__main__":
    lst = [1, 1, 2, 5, 7]
    tp = (1, 1, 2, 3, 4, 7)
    res = merge(lst, tp)
    assert res == [1, 2, 7]
    print('Test1 - OK')


    lst1 = [1, 1, 2, 5, 7]
    lst2 = [3, 6, 8]
    res = merge(lst1, lst2)
    assert res == []
    print('Test2 - OK')


    tp1 = (1, 1, 2, 2, 3, 3)
    tp2 = (1, 1, 1, 2, 2, 2, 3, 3, 3)
    res = merge(tp1, tp2)
    assert res == [1, 2, 3]
    print('Test3 - OK')

    lst1 = [1, 1, 2, 5, 7]
    lst2 = [3, 6, 8]
    res = merge(lst1, lst2)
    assert res == []
    print('Test4 - OK')
    