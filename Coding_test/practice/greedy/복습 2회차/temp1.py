# 모험가 길드
n = int(input())
nList = list(map(int, input().split()))

nList.sort()
result = 0
i = 0
while True:
    i += nList[i]
    if i >= len(nList):
        break
    result += 1

print(result)