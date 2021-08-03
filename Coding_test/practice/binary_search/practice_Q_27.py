# 정렬된 배열에서 특정 수의 개수 구하기
import bisect

n, x = map(int, input().split())
n_list = list(map(int, input().split()))


def count_by_list(num_list, start, end):
    left_idx = bisect.bisect_left(num_list, start)
    right_idx = bisect.bisect_right(num_list, end)
    result = right_idx - left_idx
    if result > 0:
        return result
    else:
        return -1


print(count_by_list(n_list, x, x))
