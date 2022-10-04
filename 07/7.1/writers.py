import csv
import json


class BaseWriter:
    def dump(self, data, fileboj):
        raise NotImplementedError


class TxtWriter(BaseWriter):
    def dump(self, data, fileobj):
        fileobj.writelines(row + '\n' for row in data)


class JsonWriter(BaseWriter):
    def dump(self, data, fileobj, **kwargs):
        json.dump(data, fileobj, **kwargs)


class CsvWriter(BaseWriter):
    def dump(self, data, fileobj, **kwargs):
        csv_writer = csv.writer(fileobj, **kwargs)
        for row in data:
            csv_writer.writerow(row)
        return data


def dump_data(data, fileobj, writer_cls=BaseWriter, **kwargs):
    writer = writer_cls()
    writer.dump(data, fileobj, **kwargs)
