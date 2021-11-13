# 징검다리 건너기
# 이분탐색 - 시작과 끝 인원수를 잡고 해당 인원으로 건넜을 때, 연속된 0이 k개 이상인지 확인
def is_jump(stones, k, mid):
    cnt = 0
    for s in stones:
        if s < mid:
            cnt += 1
        else:
            cnt = 0
        if cnt >= k:
            return True
    return False

def solution(stones, k):
    answer = 0
    start = 1
    end = int(1e8) * 2 + 1
    while start <= end:
        mid = (start + end) // 2
        if is_jump(stones, k, mid):
            end = mid - 1
        else:
            start = mid + 1
            answer = mid
    return answer

# 슬라이딩 윈도우
# def solution(stones, k):
#     n = len(stones)
#     q = stones[0:k]
#     answer = max(q)
#     for i in range(k, n):
#         # 시간복잡도 : O(n)
#         q.pop(0)
#         q.append(stones[i])
#         # 시간복잡도 : O(n)
#         max_value = max(q)
#         if answer > max_value:
#             answer = max_value
#     return answer


# union-find를 이용한 풀이(실패)
# import bisect

# def is_jump(parent, zero_list, k):
#     for x in zero_list:
#         right_idx = bisect.bisect_right(parent, x)
#         left_idx = bisect.bisect_left(parent, x)
#         if right_idx - left_idx >= k:
#             return False
#     return True

# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[b] = a
#         find_parent(parent, bisect.bisect_right(parent, b) - 1)
#     else:
#         parent[a] = b
#         find_parent(parent, bisect.bisect_right(parent, a) - 1)

# def solution(stones, k):
#     answer = 0
#     parent = [i for i in range(len(stones))]
#     stones = [(stone, i) for i, stone in enumerate(stones)]
#     zero_list = []
#     while stones:
#         # 다음 0이 되는 값 꺼내기
#         min_val, min_idx = stones.pop(stones.index(min(stones)))
#         # 현재 뛸 수 있는 상태인지 확인
#         if not is_jump(parent, zero_list, k):
#             break
#         # 뛰기
#         answer += min_val - answer
#         # 0이 된 곳 표시
#         zero_list.append(min_idx)
#         # 0이 된 곳들 연결
#         if min_idx + 1 in zero_list:
#             union_parent(parent, min_idx, min_idx + 1)
#         elif min_idx - 1 in zero_list:
#             union_parent(parent, min_idx, min_idx - 1)
#     return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
