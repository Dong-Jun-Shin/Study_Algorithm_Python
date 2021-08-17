# 떡볶이 떡 만들기
def binary_search(n_list, m):
    result = 0
    length = len(n_list) - 1
    n_list.sort()
    start = 0
    end = max(n_list)
    while start <= end:
        diff = 0
        mid = (start + end) // 2
        for i in range(length, -1, -1):
            if mid < n_list[i]:
                diff += n_list[i] - mid
            else:
                break

        if m > diff:
            end = mid - 1
        else:
            start = mid + 1
            result = mid

    return result


n, m = map(int, input().split())
n_list = list(map(int, input().split()))

print(binary_search(n_list, m))


""" Test case
4 6
19 15 10 17
"""
