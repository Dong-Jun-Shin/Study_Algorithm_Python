# 정확한 순위
n, m = map(int, input().split())
INF = int(1e9)
array = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    high, low = map(int, input().split())
    array[high][low] = 1

for i in range(n + 1):
    array[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            array[i][j] = min(array[i][j], array[i][k] + array[k][j])

count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if array[i][j] == INF and array[j][i] == INF:
            break
    else:
        count += 1
            
print(count)

""" Test case
6 6
1 5
3 4
4 2
4 6
5 2
5 4
"""
