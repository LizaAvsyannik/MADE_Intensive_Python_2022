import csv
import json


class BaseReader:
    def read(self, fileobj):
        raise NotImplementedError


class TxtReader(BaseReader):
    def read(self, fileobj):
        data = fileobj.read().splitlines()
        return data


class JsonReader(BaseReader):
    def read(self, fileobj, **kwargs):
        data = json.loads(fileobj.read(), **kwargs)
        return data


class CsvReader(BaseReader):
    def read(self, fileobj, **kwargs):
        csv_reader = csv.reader(fileobj, **kwargs)
        data = []
        for row in csv_reader:
            data.append(row)
        return data


def read_data(fileobj, reader_cls=BaseReader, **kwargs):
    reader = reader_cls()
    return reader.read(fileobj, **kwargs)
