# 금광
t = int(input())
max_list = []
for _ in range(t):
    n, m = map(int, input().split())
    array = []
    data = list(map(int, input().split()))
    for i in range(0, n * m, m):
        array.append(data[i:i + m])

    for j in range(1, m):
        for i in range(n):
            top = 0 if not(0 <= i - 1 < n) else array[i - 1][j - 1]
            bot = 0 if not(0 <= i + 1 < n) else array[i + 1][j - 1]
            mid = array[i][j - 1]
            array[i][j] = array[i][j] + max(top, mid, bot)
    
    result = 0
    for i in range(n):
        result = max(result, array[i][m - 1])

    max_list.append(result)

for max_val in max_list:
    print(max_val)
