# 부품 찾기
def binary_search(n_list, m_val):
    start = 0
    end = len(n_list) - 1

    n_list.sort()

    while start <= end:
        mid = (start + end) // 2
        if m_val > n_list[mid]:
            start = mid + 1
        elif m_val < n_list[mid]:
            end = mid - 1
        else:
            return "YES"

    return "NO"


n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for m_val in m_list:
    print(binary_search(n_list, m_val))


""" Test case
5
8 3 7 9 2
3
5 7 9
"""
