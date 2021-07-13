"""------------------------------book
# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort()
first = data[n - 1]
second = data[n - 2]

count = m // (k + 1) * k        # 가장 큰 수가 곱해지는 횟수
count += m % (k + 1)            # 반복되는 횟수(k + 1)로 나누어진 후 남는 수는 가장 큰 수이므로 덧셈

result = 0
result += (count) * first
result += (m - count) * second

print(result)
----------------------------------"""
# ---------------------------------me
inputStr = input()
inputNums = input()

listVal = inputStr.split(' ')
n = int(listVal[0])    # 배열 크기
m = int(listVal[1])    # 더하는 횟수
k = int(listVal[2])    # 동일 원소에 대한 연산 가능 횟수

listNums = inputNums.split(' ')
listNums = list(map(int, listNums))

listNums.sort(reverse=True)

sumVal = 0
while True:
    if m > k:
        sumVal += listNums[0] * k
    else:
        sumVal += listNums[0] * m

    m = m - k
    if m <= 0:
        break

    sumVal += listNums[1] * 1

    m = m - 1
    if m <= 0:
        break

print(sumVal)
# -----------------------------------
