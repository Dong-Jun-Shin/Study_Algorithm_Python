# 공유기 설치
n, c = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

n_list.sort()

start = 1
end = n_list[-1] - n_list[0]
result = 0
while start <= end:
    mid = (start + end) // 2
    val = n_list[0]
    count = 1

    for i in range(1, n):
        if n_list[i] >= val + mid:
            val = n_list[i]
            count += 1

    if c <= count:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

# 1 2 4 8 9
# x   x   x
