# 고정점 찾기
def binary_search(n_list):
    length = len(n_list) - 1
    start = 0
    end = length
    while start <= end:
        mid = (start + end) // 2
        if mid < n_list[mid]:
            end = mid - 1
        elif mid > n_list[mid]:
            start = mid + 1
        else:
            return mid

    return -1


n = int(input())
n_list = list(map(int, input().split()))

print(binary_search(n_list))


""" Test case
5
-15 -6 1 3 7

7
-15 -4 2 8 9 13 15

7
-15 -4 3 8 9 13 15
"""
