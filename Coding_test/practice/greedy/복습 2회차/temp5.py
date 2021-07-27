# 볼링공 고르기
n, m = map(int, input().split())
weightList = list(map(int, input().split()))

graph = [0] * (m + 1)
for weight in weightList:
    graph[weight] += 1

ballCnt = n
result = 0
for i in range(1, m + 1):
    ballCnt -= graph[i]
    result += graph[i] * ballCnt

print(result)