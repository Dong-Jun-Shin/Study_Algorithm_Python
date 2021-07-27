# 잃어버린 괄호
str = input()

numList = str.replace('-', '+').split('+')
operList = str
for i in range(len(numList)):
    # 문자열 안에 첫번째 매칭만 대체되도록 인수 '1' 사용
    operList = operList.replace(numList[i], ' ', 1)
    numList[i] = int(numList[i])
operList = operList.split()

result = numList[0]
# 아래 더하고 빼는 구간을 정할 때, 첫번째 마이너스 연산에 해당하는 숫자를 지정하기 위해 +1을 함
# '-'가 없을 때는 +1이 인덱스 오류를 반환하기 때문에, '+'만 있을 때는 +1이 안되도록 -1 사용
minusIdx = len(numList) - 1
if '-' in operList:
    minusIdx = operList.index('-')

if len(numList) != 1:
    for i in range(1, minusIdx + 1):
        result += numList[i]

    for i in range(minusIdx + 1, len(numList)):
        result -= numList[i]

print(result) 