from math import sqrt, isclose

def solution(a, b, c):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        return (- b + sqrt(d)) / (2 * a), (- b - sqrt(d)) / (2 * a)
    else: 
        return None


if __name__ == "__main__":
    # x^2 - 4x -5 = 0
    x = solution(1, -4, -5)
    assert(isinstance(x, tuple))
    assert isclose(x[0], 5)
    assert isclose(x[1], -1)

    # x^2  - 0.5x = 0
    x = solution(1, -0.5, 0)
    assert(isinstance(x, tuple))
    assert isclose(x[0], 0.5)
    assert isclose(x[1], 0)

    print('Tests 2 different roots - OK')

    # 2x^2  + 4x + 2 = 0
    x = solution(2, 4, 2)
    assert(isinstance(x, tuple))
    assert(isclose(x[0], -1))
    assert(isclose(x[1], -1))
    print('Test 2 equal roots - OK')

    # 4x^2 - 3x + 5 = 0
    x = solution(4, -3, 5)
    assert x is None
    print('Test no roots - OK')
