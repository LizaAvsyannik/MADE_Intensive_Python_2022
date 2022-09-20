import time

from parse_json import parse_json


def callback(word):
    time.sleep(len(word) * 1e-1 / 5)


def mean(k):
    def _mean(fn):
        counter = 0
        time_measures = []
        def wrapper(*args, **kwargs):
            nonlocal counter, k
            counter += 1

            start_time = time.time()
            res = fn(*args, **kwargs)
            time_measures.append(time.time() - start_time)

            avg_time = sum(time_measures[-k:]) / len(time_measures[-k:])

            if counter <= k:
                print(f'Average time of last {counter} function calls: {avg_time} seconds')
            else:
                print(f'Average time of last {k} function calls: {avg_time} seconds')

            return res
        return wrapper
    return _mean


if __name__ == "__main__":
    json_str = '{"key1": "Word1 word2", "key2": "word2 word3"}'

    # k < n_iterations
    k = 5
    n_iterations = 100
    timed_parse_json = mean(k)(parse_json)
    print(f'k = {k}, n_iterations = {n_iterations}')
    for i in range(n_iterations):
        timed_parse_json(json_str, callback, required_fields=["key1"], keywords=["word2"])

    print('\n')

    # k > n_iterations
    k = 100
    n_iterations = 20
    timed_parse_json = mean(k)(parse_json)
    print(f'k = {k}, n_iterations = {n_iterations}')
    for i in range(n_iterations):
        timed_parse_json(json_str, callback, required_fields=["key1"], keywords=["word2"])
