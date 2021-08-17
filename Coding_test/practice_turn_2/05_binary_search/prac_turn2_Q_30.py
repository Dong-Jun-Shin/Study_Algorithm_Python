# 가사 검색
import bisect


def get_count(words, start, end):
    left_idx = bisect.bisect_left(words, start)
    right_idx = bisect.bisect_right(words, end)
    return right_idx - left_idx


def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]

    for word in words:
        w_length = len(word)
        array[w_length].append(word)
        reverse_array[w_length].append(word[::-1])

    # queries는 10만까지 나올 수 있고 array는 1만까지만 나오기 때문에, 따로 정렬을 처리
    for i in range(len(array)):
        array[i].sort()
        reverse_array[i].sort()

    for querie in queries:
        q_length = len(querie)
        compare_list = array[q_length]

        if querie[0] == '?' and querie[-1] != '?':
            querie = querie[::-1]
            compare_list = reverse_array[q_length]

        start = querie.replace('?', 'a')
        end = querie.replace('?', 'z')
        answer.append(get_count(compare_list, start, end))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
