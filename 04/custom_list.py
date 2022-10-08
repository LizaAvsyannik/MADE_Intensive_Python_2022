from itertools import zip_longest


class CustomList(list):
    @property
    def lst(self):
        return list(self)

    @lst.setter
    def lst(self, val):
        self.__init__(val)

    def __add__(self, other):
        res = [sum(el) for el in zip_longest(self, other, fillvalue=0)]
        return CustomList(res)

    def __sub__(self, other):
        min_length = min(len(self), len(other))
        res = []
        for i in range(min_length):
            res.append(self[i] - other[i])
        if min_length == len(self):
            res.extend(other[min_length:])
        else:
            res.extend(self[min_length:])
        return CustomList(res)

    def __radd__(self, other):
        return self.__add__(CustomList(other))

    def __rsub__(self, other):
        return self.__sub__(CustomList(other))

    def __lt__(self, other):
        return sum(self) < sum(other)

    def __le__(self, other):
        return sum(self) <= sum(other)

    def __eq__(self, other):
        return sum(self) == sum(other)

    def __ne__(self, other):
        return sum(self) != sum(other)

    def __gt__(self, other):
        return sum(self) > sum(other)

    def __ge__(self, other):
        return sum(self) >= sum(other)

    def __str__(self):
        return f'{super().__str__()}, {sum(self)}'
