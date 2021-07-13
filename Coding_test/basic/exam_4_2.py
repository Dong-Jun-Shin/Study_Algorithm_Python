""" 3중 for문은 100만개 이하의 데이터를 완전탐색으로 처리할 때 적절하다 """
"""------------------------------book
# H를 입력받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1

print(count)
----------------------------------"""

# ---------------------------------me
"""
1시간 동안 초에서 3이 나오는 경우의 수 15번
0:00:0,1,2,3,4,5 3
0:00:3 0,1,2,3,4,5,6,7,8,9

1시간 동안 분에서 3이 나오는 경우의 수 15번
0:0,1,2,3,4,5 3:00
0:3 0,1,2,3,4,5,6,7,8,9:00

전체 시간 경우의 수 : (n + 1) 60 60
시, 분, 초 각각 3이 포함된 경우의 수 : m 15 15

3이 하나라도 포함된 경우의 수 :
((n + 1) * 60 * 60) - ((n + 1 - m) * (60 - 15) * (60 - 15))

"""

hour = int(input())

hourCnt = 0

for i in range(hour):
    hourStr = str(i)
    if hourStr.find('3') != -1:
        hourCnt += 1

totalCase = (hour + 1) * 60 * 60
selectCase = (hour + 1 - hourCnt) * (60 - 15) * (60 - 15)

result = totalCase - selectCase

print(result)
# -----------------------------------
