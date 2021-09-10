# 가사 검색
import bisect


def get_count(word_list, start, end):
    right_idx = bisect.bisect_right(word_list, end)
    left_idx = bisect.bisect_left(word_list, start)
    return right_idx - left_idx


def get_equal_cnt(querie, word_list, r_word_list):
    len_querie = len(querie)
    words = word_list[len_querie]
    if querie[0] == "?" and querie[-1] != "?":
        querie = querie[::-1]
        words = r_word_list[len_querie]

    start = querie.replace('?', 'a')
    end = querie.replace('?', 'z')
    return get_count(words, start, end)


def solution(words, queries):
    answer = []
    word_list = [[] for _ in range(10001)]
    r_word_list = [[] for _ in range(10001)]
    for word in words:
        len_word = len(word)
        word_list[len_word].append(word)
        r_word_list[len_word].append(word[::-1])

    for i in range(len(word_list)):
        word_list[i].sort()
        r_word_list[i].sort()

    for querie in queries:
        answer.append(get_equal_cnt(querie, word_list, r_word_list))
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
