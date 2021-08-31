# 플로이드
n = int(input())
m = int(input())

INF = int(1e9)
array = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(n + 1):
    array[i][i] = 0

for _ in range(m):
    start, end, cost = map(int, input().split())
    array[start][end] = min(array[start][end], cost)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            array[i][j] = min(array[i][j], array[i][k] + array[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(array[i][j] if array[i][j] != INF else 0, end=" ")
    print()
