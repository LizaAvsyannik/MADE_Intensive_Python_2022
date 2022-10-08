from custom_list import CustomList


c_lst1 = CustomList([5, 1, 3, 7])
c_lst2 = CustomList([1, 2, 7])

# sum
c_lst_sum = c_lst1 + c_lst2
assert isinstance(c_lst_sum, CustomList)
assert c_lst_sum.lst == [6, 3, 10, 7]
assert c_lst1.lst == [5, 1, 3, 7]
assert c_lst2.lst == [1, 2, 7]

# sub
c_lst_sub = c_lst1 - c_lst2
assert isinstance(c_lst_sub, CustomList)
assert c_lst_sub.lst == [4, -1, -4, 7]
assert c_lst1.lst == [5, 1, 3, 7]
assert c_lst2.lst == [1, 2, 7]

# with list
lst = [1, 2, 3, 4]
c_lst = CustomList([3, 4])

c_lst_sum = c_lst + lst
assert isinstance(c_lst_sum, CustomList)
assert c_lst_sum.lst == [4, 6, 3, 4]
assert c_lst.lst == [3, 4]
assert lst == [1, 2, 3, 4]

c_lst_sub = c_lst - lst
assert isinstance(c_lst_sub, CustomList)
assert c_lst_sub.lst == [2, 2, 3, 4]
assert c_lst.lst == [3, 4]
assert lst == [1, 2, 3, 4]

c_lst_sum = lst + c_lst
assert isinstance(c_lst_sum, CustomList)
assert c_lst_sum.lst == [4, 6, 3, 4]
assert c_lst.lst == [3, 4]
assert lst == [1, 2, 3, 4]

c_lst_sub = lst - c_lst
assert isinstance(c_lst_sub, CustomList)
assert c_lst_sub.lst == [2, 2, 3, 4]
assert c_lst.lst == [3, 4]
assert lst == [1, 2, 3, 4]

# comparisons
assert not (c_lst1 < c_lst2)

c_lst1.append(-8)
assert c_lst1 <= c_lst2

c_lst1.append(2)
assert c_lst1 == c_lst2

c_lst2.append(5)
assert c_lst1 != c_lst2

assert not (c_lst2 < c_lst1)

c_lst2.append(-5)
assert c_lst2 >= c_lst1

# str
assert str(c_lst1) == '[5, 1, 3, 7, -8, 2], 10'
assert str(c_lst2) == '[1, 2, 7, 5, -5], 10'
