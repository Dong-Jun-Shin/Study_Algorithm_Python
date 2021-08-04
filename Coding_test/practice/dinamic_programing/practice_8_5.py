# 효율적인 화폐 구성
n, m = map(int, input().split())
n_list = []
for _ in range(n):
    n_list.append(int(input()))

d = [10001] * (m + 1)
d[0] = 0
for val in n_list:
    for i in range(val, m + 1):
        d[i] = min(d[i], d[i - val] + 1)

print(d[m] if d[m] != 10001 else -1)
