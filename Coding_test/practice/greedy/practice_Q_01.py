# 모험가 길드
n = int(input())
people = list(map(int, input().split()))

people.sort()
groupCnt = 0

for person in people:
    if n <= person:
        break
    n -= person
    groupCnt += 1

print(groupCnt)
