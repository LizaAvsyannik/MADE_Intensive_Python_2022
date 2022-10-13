import unittest

from lru_cache import LRUCache

# solution has passed LeetCodes's problem:
# https://leetcode.com/problems/lru-cache/
# submission: https://leetcode.com/submissions/detail/812586394/


class TestLRUCache(unittest.TestCase):
    def test1_example(self):
        lru_cache = LRUCache(2)

        lru_cache.put("k1", "val1")
        lru_cache.put("k2", "val2")

        self.assertEqual(lru_cache.get("k3"), None)
        self.assertEqual(lru_cache.get("k2"), "val2")
        self.assertEqual(lru_cache.get("k1"), "val1")

        lru_cache.put("k3", "val3")

        self.assertEqual(lru_cache.get("k3"), "val3")
        self.assertEqual(lru_cache.get("k2"), None)
        self.assertEqual(lru_cache.get("k1"), "val1")

    def test2(self):
        lru_cache = LRUCache(2)

        lru_cache.put("k1", "val1")
        lru_cache.put("k2", "val2")
        self.assertEqual(lru_cache.get("k1"), "val1")

        lru_cache.put("k3", "val3")
        self.assertEqual(lru_cache.get("k2"), None)

        lru_cache.put("k4", "val4")
        self.assertEqual(lru_cache.get("k1"), None)
        self.assertEqual(lru_cache.get("k3"), "val3")
        self.assertEqual(lru_cache.get("k4"), "val4")

    def test3_with_change_existing_key(self):
        lru_cache = LRUCache(2)

        lru_cache.put("k2", "val1")
        lru_cache.put("k2", "val2")  # exists

        self.assertEqual(lru_cache.get("k2"), "val2")

        lru_cache.put("k1", "val1")
        lru_cache.put("k4", "val1")

        self.assertEqual(lru_cache.get("k2"), None)

    def test4_with_change_existing_key(self):
        lru_cache = LRUCache(3)

        lru_cache.put("k2", "val1")
        lru_cache.put("k1", "val1")
        lru_cache.put("k3", "val3")

        self.assertEqual(lru_cache.get("k2"), "val1")

        lru_cache.put("k1", "val2")  # exists
        self.assertEqual(lru_cache.get("k1"), "val2")
        self.assertEqual(lru_cache.get("k2"), "val1")

        lru_cache.put("k4", "val4")
        self.assertEqual(lru_cache.get("k3"), None)
        self.assertEqual(lru_cache.get("k1"), "val2")

    def test5_one_capacity(self):
        lru_cache = LRUCache(1)

        lru_cache.put("k1", "val1")
        lru_cache.put("k2", "val2")

        self.assertEqual(lru_cache.get("k1"), None)
        self.assertEqual(lru_cache.get("k2"), "val2")

        lru_cache.put("k3", "val3")
        self.assertEqual(lru_cache.get("k2"), None)
        self.assertEqual(lru_cache.get("k3"), "val3")


if __name__ == "__main__":
    unittest.main()
