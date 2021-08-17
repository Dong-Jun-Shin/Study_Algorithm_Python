# 정렬된 배열에서 특정 수의 개수 구하기
import bisect


def get_count(n_list, x):
    left_idx = bisect.bisect_left(n_list, x)
    right_idx = bisect.bisect_right(n_list, x)
    return right_idx - left_idx


n, x = map(int, input().split())
n_list = list(map(int, input().split()))
result = get_count(n_list, x)
if result == 0:
    print("-1")
else:
    print(result)

""" Test case
7 2
1 1 2 2 2 2 3

7 4
1 1 2 2 2 2 3
"""
