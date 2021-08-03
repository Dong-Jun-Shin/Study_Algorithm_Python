# 떡볶이 떡 만들기
n, m = map(int, input().split())
n_list = list(map(int, input().split()))

if sum(n_list) == m:
    print(0)

n_list.sort()

start = 0           # 떡 시작 길이
end = n_list[-1]    # 최대 떡 길이

result = 0
while start <= end:
    mid = (start + end) // 2

    sum_val = 0
    for val in n_list:
        if val > mid:
            sum_val += val - mid

    if sum_val < m:
        end = mid - 1
    else:
        start = mid + 1
        result = mid

print(result)
