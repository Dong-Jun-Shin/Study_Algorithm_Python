# 최종 순위
from collections import deque

for _ in range(int(input())):
    n = int(input())
    prev_rank = list(map(int, input().split()))
    degrees = [0] * (n + 1)
    array = [[False] * (n + 1) for _ in range(n + 1)]
    for i in range(len(prev_rank)):
        for j in prev_rank[i + 1:]:
            array[prev_rank[i]][j] = True
        degrees[prev_rank[i]] = i

    m = int(input())
    for _ in range(m):
        a, b = map(int, input().split())
        if array[a][b]:
            array[a][b] = False
            array[b][a] = True
            degrees[a] += 1
            degrees[b] -= 1
        else:
            array[a][b] = True
            array[b][a] = False
            degrees[a] -= 1
            degrees[b] += 1

    q = deque()
    for i in range(1, len(degrees)):
        if degrees[i] == 0:
            q.append(i)
    result = ""
    cycle = False
    certain = True
    for _ in range(n):
        if len(q) > 1:
            certain = False
            break
        if len(q) == 0:
            cycle = True
            break
        s_idx = q.popleft()
        result += f"{s_idx} "
        for i in range(1, n + 1):
            if array[s_idx][i]:
                degrees[i] -= 1
                if degrees[i] == 0:
                    q.append(i)

    if cycle:
        result = "IMPOSSIBLE"
    elif not certain:
        result = "?"

    print(result)
