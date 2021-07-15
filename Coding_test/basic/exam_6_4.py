# 정렬할 숫자 리스트 받기
numList = list(map(int, input()))

# 입력받은 리스트의 최대 값 크기를 가진 카운트 리스트 생성
sortList = [0] * (max(numList) + 1)

# 입력받은 리스트를 카운트
for i in range(len(numList)):
    sortList[numList[i]] += 1

# 입력받은 카운트 리스트에 따라 정렬된 값을 출력
for i in range(len(sortList)):
    for j in range(sortList[i]):
        print(i, end=' ')
