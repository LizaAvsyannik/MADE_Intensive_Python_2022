import unittest
from io import StringIO

from writers import TxtWriter, JsonWriter, CsvWriter, dump_data
from readers import TxtReader, JsonReader, CsvReader, read_data


class TestIO(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer = StringIO()

    def test_base_writer(self):
        with self.assertRaises(NotImplementedError):
            data = 'test base writer'
            dump_data(data, self.buffer)

    def test_base_reader(self):
        with self.assertRaises(NotImplementedError):
            read_data(self.buffer)

    def test_txt_io(self):
        data = ['aaa', 'bbb', 'ccc']
        dump_data(data, self.buffer, writer_cls=TxtWriter)
        self.assertEqual(self.buffer.getvalue(), 'aaa\nbbb\nccc\n')

        self.buffer.seek(0)
        data = read_data(self.buffer, reader_cls=TxtReader)
        self.assertEqual(data, ['aaa', 'bbb', 'ccc'])

    def test_json_io(self):
        data = {'aaa': 3, 'bbb': 2, 'ccc': 1}
        dump_data(data, self.buffer, writer_cls=JsonWriter)
        self.assertEqual(self.buffer.getvalue(), '{"aaa": 3, "bbb": 2, "ccc": 1}')

        self.buffer.seek(0)
        data = read_data(self.buffer, reader_cls=JsonReader)
        self.assertEqual(data, {'aaa': 3, 'bbb': 2, 'ccc': 1})

    def test_csv_io(self):
        data = [['aaa', 'bbb', 'ccc'], ['ddd', 'eee', 'fff']]
        dump_data(data, self.buffer, writer_cls=CsvWriter, delimiter='|', lineterminator='\n')
        self.assertEqual(self.buffer.getvalue(), 'aaa|bbb|ccc\nddd|eee|fff\n')

        self.buffer.seek(0)
        data = read_data(self.buffer, reader_cls=CsvReader, delimiter='|', lineterminator='\n')
        self.assertEqual(data, [['aaa', 'bbb', 'ccc'], ['ddd', 'eee', 'fff']])


if __name__ == "__main__":
    unittest.main()
