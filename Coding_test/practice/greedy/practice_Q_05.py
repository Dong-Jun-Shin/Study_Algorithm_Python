# 볼링공 고르기
n, m = map(int, input().split())
weightList = list(map(int, input().split()))

""" ------------------------------------book
array = [0] * 11
for weight in weightList:
    array[weight] += 1

count = 0
for i in range(1, m + 1):
    n -= array[i]           # 무게가 i인 공의 개수를 차감 (=B가 선택할 공의 개수)
    count += array[i] * n   # A가 선택할 경우의 수 * B가 선택하는 경우의 수
"""
# ----------------------------------------me
count = 0
for i in range(len(weightList)):
    for j in range(i, len(weightList)):
        if weightList[i] == weightList[j]:
            continue
        count += 1
# ------------------------------------------

print(count)
