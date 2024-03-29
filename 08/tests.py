import unittest

from search_anagrams import find_anagrams

# solution has passed LeetCodes's problem: https://leetcode.com/problems/find-all-anagrams-in-a-string/
# submission: https://leetcode.com/submissions/detail/817637490/


class TestFindAnagrams(unittest.TestCase):
    def test1(self):
        self.assertEqual(find_anagrams('cbaebabacd', 'abc'), [0, 6])

    def test2(self):
        self.assertEqual(find_anagrams('aaaaaaaaaa', 'aaaaaaaaaaaaa'), [])

    def test3(self):
        self.assertEqual(find_anagrams('aaaaaaaaaaaaa', 'aaaaaaaaaa'), [0, 1, 2, 3])

    def test4(self):
        self.assertEqual(find_anagrams('abc', 'deb'), [])

    def test5(self):
        self.assertEqual(find_anagrams('', 'deb'), [])

    def test6(self):
        self.assertEqual(find_anagrams('abc', ''), [])

    def test7(self):
        self.assertEqual(find_anagrams('', ''), [])


if __name__ == "__main__":
    unittest.main()
