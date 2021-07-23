# 큰 수의 법칙
n, m, k = map(int, input().split())
numList = list(map(int, input().split()))

numList.sort()

first = numList[n - 1]
second = numList[n - 2]

firstCount = m // (k + 1) * k
firstCount += m % (k + 1)
secondCount = m - firstCount

result = 0
result += first * firstCount
result += second * secondCount

print(result)
