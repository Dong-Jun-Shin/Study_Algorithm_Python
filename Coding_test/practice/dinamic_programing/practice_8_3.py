# 개미 전사
n = int(input())
n_list = list(map(int, input().split()))

d = [0] * 100
d[0] = n_list[0]
d[1] = max(n_list[0], n_list[1])
for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + n_list[i])

print(d[n - 1])
