import io

from exceptions import EmptyFileNameError, EmptySearchWordsError


class FileFilteringGenerator():
    def __init__(self, file, search_words=None):
        if not search_words:
            raise EmptySearchWordsError('Words for search is an empty list')

        if isinstance(file, str):
            if not file:
                raise EmptyFileNameError('File Name is an empty string')
            self.__is_fileobj = False
            self.__file_name = file
        elif isinstance(file, io.IOBase):
            self.__is_fileobj = True
            self.__fileobj = file
        else:
            raise TypeError

        self.__search_words = [word.lower() for word in search_words]

    def __iter__(self):
        try:
            if self.__is_fileobj:
                while True:
                    line = self.__fileobj.readline().strip()
                    if not line:
                        raise StopIteration
                    if set(self.__search_words) & set(line.lower().split()):
                        yield line
            else:
                with open(self.__file_name, 'r') as fileobj:
                    while True:
                        line = fileobj.readline().strip()
                        if not line:
                            raise StopIteration
                        if set(self.__search_words) & set(line.lower().split()):
                            yield line
        except StopIteration:
            return
