# 곱하기 혹은 더하기
strList = list(map(int, input()))

result = 0
for str in strList:
    if str <= 1 or result == 0:
        result += str
    else:
        result *= str

print(result)
