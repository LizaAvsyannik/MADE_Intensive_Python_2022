from custom_list import CustomList


c_lst1 = CustomList([5, 1, 3, 7])
c_lst2 = CustomList([1, 2, 7])

# sum
c_lst_sum = c_lst1 + c_lst2
assert type(c_lst_sum).__name__ == 'CustomList'
assert c_lst_sum.lst == [6, 3, 10, 7]

# sub
c_lst_sub = c_lst1 - c_lst2
assert type(c_lst_sub).__name__ == 'CustomList'
assert c_lst_sub.lst == [4, -1, -4, 7]

# with list
lst = [1, 2]
c_lst = CustomList([3, 4])

c_lst_sum = c_lst + lst
assert type(c_lst_sum).__name__ == 'CustomList'
assert c_lst_sum.lst == [4, 6]

c_lst_sub = c_lst - lst
assert type(c_lst_sub).__name__ == 'CustomList'
assert c_lst_sub.lst == [2, 2]

c_lst_sum = lst + c_lst
assert type(c_lst_sum).__name__ == 'CustomList'
assert c_lst_sum.lst == [4, 6]

c_lst_sub = lst - c_lst
assert type(c_lst_sub).__name__ == 'CustomList'
assert c_lst_sub.lst == [2, 2]

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
print('Method str:')
print(c_lst1)
print(c_lst2)
