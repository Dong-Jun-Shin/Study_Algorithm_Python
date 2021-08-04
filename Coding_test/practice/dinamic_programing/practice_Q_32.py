# 정수 삼각형
n = int(input())
n_list = []
for _ in range(n):
    n_list.append(list(map(int, input().split())))

result = 0
for i in range(1, n):
    for j in range(i + 1):
        left = 0 if not (0 <= j - 1 < i) else n_list[i - 1][j - 1]
        right = 0 if not (0 <= j < i) else n_list[i - 1][j]
        n_list[i][j] = n_list[i][j] + max(left, right)


print(max(n_list[n - 1]))
