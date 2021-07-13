# 행, 열 받기
n, m = map(int, input().split())

cardArr = [list] * n
result = 0

# 카드 숫자 받기
for i in range(n):
    cardArr[i] = list(map(int, input().split()))

# 행마다 최솟값을 비교
for i in range(n):
    val = min(cardArr[i])
    if result < val:
        result = val

# 선택한 최솟값 출력
print(result)
