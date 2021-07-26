# 잃어버린 괄호
import copy

numList = input()
operList = copy.deepcopy(numList)

# 숫자 리스트로 만들기
numList = numList.replace('-', '+').split('+')
# 연산 리스트로 만들기
for i in range(len(numList)):
        operList = operList.replace(numList[i], ' ', 1)
numList = list(map(int, numList))
operList = list(operList.split())

# 첫번째 빼기 연산 위치 찾기
separIdx = 0
if '-' in operList:
    separIdx = operList.index('-') + 1

result = 0
if separIdx != 0:
    for i in range(0, separIdx):
        result += numList[i]
    for i in range(separIdx, len(numList)):
        result -= numList[i]
else:
    # 더하기만 있는 경우
    for i in range(0, len(numList)):
        result += numList[i]
   
print(result)

"""
테스트 케이스
----------------------일반적인 경우
55-50-40 = -35
50+50-100+100-100-100 = -300
43-43+45-45 = -90
----------------------0으로 시작하는 양수와 0을 표기한 양수의 경우
0-101-01 = -102
0000-10000+1+0111+0111+01111 = -11334
----------------------양수 2개를 빼는 경우
4-09 = -5
1-1 = 0
----------------------0으로 시작하는 경우, 양수만 나온 경우
0555 = 555
----------------------더하기만 하는 경우
05+060 = 65
"""