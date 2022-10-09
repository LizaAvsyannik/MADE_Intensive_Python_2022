import unittest
from io import StringIO

from generator import FileFilteringGenerator
from exceptions import EmptyFileNameError, EmptySearchWordsError


class TestIO(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.buffer = StringIO()

    def test_empty_file_name(self):
        with self.assertRaises(EmptyFileNameError, msg='File Name is an empty string'):
            FileFilteringGenerator('', ['a', 'b', 'c'])

    def test_empty_search_words(self):
        with self.assertRaises(EmptySearchWordsError, msg='Words for search is an empty list'):
            FileFilteringGenerator('test.txt', [])

    def test_type_error(self):
        with self.assertRaises(TypeError):
            FileFilteringGenerator(1, ['a', 'b', 'c'])

    def test_generator_next(self):
        data = ['aaa bbb', 'ccc ddd', 'bbb AAA']
        self.buffer.writelines(row + '\n' for row in data)

        self.buffer.seek(0)
        gen = iter(FileFilteringGenerator(self.buffer, ['aaa']))

        self.assertEqual(next(gen), 'aaa bbb')
        self.assertEqual(next(gen), 'bbb AAA')

        with self.assertRaises(StopIteration):
            next(gen)

    def test_generator_for(self):
        data = ['aaa bbb', 'ccc ddd', 'bbb AAA',
                'CCC ddd eee', 'EEE bbb aaa']
        self.buffer.writelines(row + '\n' for row in data)

        self.buffer.seek(0)
        gen = iter(FileFilteringGenerator(self.buffer, ['ccc', 'EEE']))

        filtered = []
        for i in gen:
            filtered.append(i)

        self.assertEqual(filtered, ['ccc ddd', 'CCC ddd eee', 'EEE bbb aaa'])

    def test_generator_file_name(self):
        gen = iter(FileFilteringGenerator('test.txt', ['aaa']))

        self.assertEqual(next(gen), 'aaa bbb')
        self.assertEqual(next(gen), 'bbb AAA')

        with self.assertRaises(StopIteration):
            next(gen)


if __name__ == "__main__":
    unittest.main()
