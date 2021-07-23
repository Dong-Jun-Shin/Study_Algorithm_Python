# 볼링공 고르기
n, m = map(int, input().split())
weightList = list(map(int, input().split()))

count = 0
for i in range(len(weightList)):
    for j in range(i, len(weightList)):
        if weightList[i] == weightList[j]:
            continue
        count += 1

print(count)
