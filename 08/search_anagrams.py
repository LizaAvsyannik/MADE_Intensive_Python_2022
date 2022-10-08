from typing import List


N_LETTERS = 26
SHIFT = ord('a')


def check_less(cnt_t, cnt_s):
    for i in range(N_LETTERS):
        if cnt_t[i] < cnt_s[i]:
            return False
    return True


def find_anagrams(text: str, pattern: str) -> List[int]:
    if not text or not pattern:
        return []

    s = text.lower()
    p = pattern.lower()
    n = len(s)
    m = len(p)

    cnt_p = [0] * N_LETTERS
    cnt_s = [0] * N_LETTERS
    cnt_s[ord(s[0]) - SHIFT] += 1
    for sym in p:
        cnt_p[ord(sym) - SHIFT] += 1

    i = 0
    start = 0
    result = []

    while (i < n and start < n):
        if start <= i:
            if i - start == m - 1:
                if cnt_p == cnt_s:
                    result.append(start)
                cnt_s[ord(s[start]) - SHIFT] -= 1
                start += 1
                i += 1
                if i == n:
                    break
                cnt_s[ord(s[i]) - SHIFT] += 1
            else:
                if check_less(cnt_p, cnt_s):
                    i += 1
                    if i == n:
                        break
                    cnt_s[ord(s[i]) - SHIFT] += 1
                else:
                    cnt_s[ord(s[start]) - SHIFT] -= 1
                    start += 1
        else:
            i += 1
            if i == n:
                break
            cnt_s[ord(s[i]) - SHIFT] += 1

    return result
