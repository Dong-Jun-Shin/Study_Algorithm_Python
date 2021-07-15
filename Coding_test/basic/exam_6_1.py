# 정렬할 숫자 리스트 받기
numList = list(map(int, input()))

# 선택 정렬
for i in range(len(numList)):
    for j in range(i + 1, len(numList)):
        min_index = i
        if numList[i] > numList[j]:
            numList[i], numList[j] = numList[j], numList[i]

print(numList)
