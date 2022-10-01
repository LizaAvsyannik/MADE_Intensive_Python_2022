import unittest

from lru_cache import LRUCache

# solution has passed LeetCodes's problem: https://leetcode.com/problems/lru-cache/
# submission: https://leetcode.com/submissions/detail/812586394/


class TestLRUCache(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.scenarios = [{'methods': ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"],
                           'inputs': [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]],
                           'results': [1, -1, -1, 3, 4]},
                          {'methods': ["LRUCache", "put", "put", "get", "put", "put", "get"],
                           'inputs': [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]],
                           'results': [2, -1]}, 
                          {'methods': ["LRUCache", "put", "put", "put",  "get", "put", "get", "put", "get", "get"],
                           'inputs': [[3], [2, 1], [1, 1], [3, 3], [2], [1, 2], [2], [4, 4], [3], [1]],
                           'results': [1, 1, -1, 2]}]

    def test_cache(self):

        def test_scene(scene):
            result = []
            for i in range(len(scene['methods'])):
                if scene['methods'][i] == 'LRUCache':
                    capacity = scene['inputs'][i][0]
                    lru_cache = LRUCache(capacity)
                elif scene['methods'][i] == 'put':
                    key, value = scene['inputs'][i][0], scene['inputs'][i][1]
                    lru_cache.put(key, value)
                else:
                    key = scene['inputs'][i][0]
                    result.append(lru_cache.get(key))
            self.assertEqual(result, scene['results'])

        for scene in self.scenarios:
            test_scene(scene)


if __name__ == "__main__":
    unittest.main()
