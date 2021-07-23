# 숫자 카드 게임
n, m = map(int, input().split())
numList = []
for _ in range(n):
    numList.append(list(map(int, input().split())))

valList = []
for i in range(len(numList)):
    valList.append(min(numList[i]))

print(max(valList))
