import json
from collections import defaultdict, OrderedDict


def word_statistics(word):
    global stats
    stats[word] += 1


def parse_json(json_str: str, keyword_callback, required_fields=None, keywords=None):
    if json_str == '':
        print('JSON is an empty string')
        return
    elif required_fields == None:
        print('No required fields specified')
        return
    elif keywords == None:
        print('No keywords specified')
        return

    json_doc = json.loads(json_str)
    json_doc = {k.lower(): v.lower().split() for k, v in json_doc.items()}

    for field in required_fields:
        if field in json_doc.keys():
            words = json_doc[field]
            words_intersection = set(words).intersection(set(keywords))
            for w in words_intersection:
                keyword_callback(w)
        else:
            print(f'No key - {field} in JSON')


if __name__ == "__main__":
    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key1"], keywords=["word2"])

    assert stats == {'word2': 1}
    print('Test1 - OK\n')

    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key1", "key2"], keywords=["word2", "word3"])

    assert(OrderedDict(stats)) == {"word2": 2, "word3": 1}
    print('Test2 - OK\n')

    json_str = ''
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key1", "key2"], keywords=["word2", "word3"])

    assert stats == {}
    print('Test3 empty json - OK\n')

    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=None, keywords=["word2", "word3"])

    assert stats == {}
    print('Test4 no required fields - OK\n')

    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key1", "key2"], keywords=None)

    assert stats == {}
    print('Test5 no required fields - OK\n')

    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key3"], keywords=["word2"])

    assert stats == {}
    print('Test5 no such field - OK\n')

    json_str = '{"key1": "Word1 word2 word4", "key2": "word2 word3", "key3": "word2 word3 word4", "key4": "word1 word3"}'
    stats = defaultdict(lambda: 0)
    parse_json(json_str, word_statistics, required_fields=["key3", "key4"], keywords=["word0", "word2", "word3", "word4"])

    assert OrderedDict(stats) == {"word2": 1, "word3": 2, "word4": 1}
    print('Test6 - OK\n')
