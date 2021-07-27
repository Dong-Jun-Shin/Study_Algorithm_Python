# 회의실 배정
n = int(input())
graph = []
for i in range(n):
    start, end = map(int, input().split())
    graph.append((start, end))

graph.sort(key=lambda x: (x[1], x[0]))

endTime = graph[0][1]
result = 1
for i in range(1, n):
    if graph[i][0] >= endTime:
        endTime = graph[i][1]
        result += 1

print(result)
