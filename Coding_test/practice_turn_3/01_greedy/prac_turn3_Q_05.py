# 볼링공 고르기
n, m = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort()
result = 0
for i in range(n):
    for j in range(i + 1, n):
        if n_list[i] == n_list[j]:
            continue
        result += 1

print(result)

"""
1 3 2 3 2
1 2 2 3 3

1 = 4
2 = 3
3 = 3

1 = 4
2 = 2
2 = 2

1 5 4 3 2 4 5 2
1 2 2 3 4 4 5 5

1 = 7
2 = 5
2 = 5
3 = 4
4 = 2
4 = 2

25
"""
