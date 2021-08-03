# 가사 검색(길이별로 문자 분류, 정렬된 문자열 리스트에 이진탐색으로 삽입할 곳을 찾고 개수를 세는게 핵심)
import bisect


def count_by_value(array, start, end):
    left_count = bisect.bisect_left(array, start)
    right_count = bisect.bisect_right(array, end)
    return (right_count - left_count)

def solution(words, queries):
    answer = []
    array = [[] for _ in range(10001)]
    reverse_array = [[] for _ in range(10001)]
    for word in words:
        array[len(word)].append(word)
        reverse_array[len(word)].append(word[::-1])

    for i in range(len(array)):
        array[i].sort()
        reverse_array[i].sort()

    for querie in queries:
        if querie[0] != '?':
            answer.append(count_by_value(array[len(querie)], querie.replace('?', 'a'), querie.replace('?', 'z')))
        else:
            answer.append(count_by_value(reverse_array[len(querie)], querie[::-1].replace('?', 'a'), querie[::-1].replace('?', 'z')))

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

# ---------------------------------------------------------------- me(선형 탐색)
# def get_index(querie):
#     start, end, direction = 0, len(querie), 0
#     if querie[0] != '?':
#         direction = 1
#     elif querie[-1] == '?':
#         direction = 2
    
#     if direction == 0:
#         for i in range(len(querie)):
#             if querie[i] != '?':
#                 start = i
#                 break
#     elif direction == 1:
#         for i in range(len(querie) - 1, -1, -1):
#             if querie[i] != '?':
#                 end = i + 1
#                 break

#     return (start, end, direction)

# def solution(words, queries):
#     answer = []
#     for querie in queries:
#         start, end, direction = get_index(querie)
#         length = len(querie)
#         count = 0
#         for word in words:
#             if len(word) == length:
#                 if direction == 2:
#                     count += 1
#                 else:
#                     if word.find(querie[start:end], start, end) != -1:
#                         count += 1
#         answer.append(count)
#     return answer
# ---------------------------------------------------------------- me
