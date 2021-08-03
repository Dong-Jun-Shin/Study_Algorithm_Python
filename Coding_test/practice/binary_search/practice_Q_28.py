# 고정점 찾기
n = int(input())
n_list = list(map(int, input().split()))

start = 0
end = len(n_list) - 1

while True:
    if start > end:
        print(-1)
        break

    mid = (start + end) // 2

    if mid == n_list[mid]:
        print(mid)
        break
    elif mid > n_list[mid]:
        start += 1
    elif mid < n_list[mid]:
        end -= 1
