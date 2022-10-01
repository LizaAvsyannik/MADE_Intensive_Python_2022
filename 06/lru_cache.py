class LRUCache():
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__cache = {}
        self.__recents = []
        self.__size = 0

    def get(self, key):
        if key in self.__cache:
            self.__recents.pop(self.__recents.index(key))
            self.__recents.append(key)
            return self.__cache[key]
        else:
            return -1

    def put(self, key, value):
        if key in self.__cache:
            self.__recents.pop(self.__recents.index(key))
        else:
            if self.__capacity >= (self.__size + 1):
                self.__size += 1
            else:
                least_recently_used = self.__recents.pop(0)
                self.__cache.pop(least_recently_used)
        self.__cache[key] = value
        self.__recents.append(key)
