from itertools import zip_longest


class CustomList(list):
    def __init__(self, *args):
        super().__init__(*args)
        self.__sum = sum(self)

    @property
    def lst(self):
        return list(self)

    @lst.setter
    def lst(self, val):
        self.__init__(val)

    @property
    def sum(self):
        return self.__sum

    @sum.setter
    def sum(self, val):
        raise AttributeError('Sum is read-only')

    def update_sum(self):
        self.__sum = sum(self)

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
        self.update_sum()
        other.update_sum()
        return self.__sum < other.sum

    def __le__(self, other):
        self.update_sum()
        other.update_sum()
        return self.__sum <= other.sum

    def __eq__(self, other):
        self.update_sum()
        other.update_sum()
        return self.__sum == other.sum

    def __ne__(self, other):
        self.update_sum()
        other.update_sum()
        return self.__sum != other.sum

    def __gt__(self, other):
        self.update_sum()
        other.update_sum()
        return self.__sum > other.sum

    def __ge__(self, other):
        self.update_sum()
        other.update_sum()
        return self.__sum >= other.sum

    def __str__(self):
        self.update_sum()
        return f'{super().__str__()}, {self.__sum}'
