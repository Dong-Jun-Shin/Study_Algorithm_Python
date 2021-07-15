# 정렬할 숫자 리스트 받기
numList = list(map(int, input()))

# 삽입 정렬
for i in range(len(numList)):
    for j in range(i, 0, -1):
        if numList[j] < numList[j - 1]:
            numList[j], numList[j - 1] = numList[j - 1], numList[j]
        else:
            break

print(numList)
