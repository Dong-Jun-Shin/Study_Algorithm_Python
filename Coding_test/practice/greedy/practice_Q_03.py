# 문자열 뒤집기
strList = list(map(int, input()))

count = 0
for i in range(1, len(strList)):
    if strList[i] != strList[0] and strList[i] != strList[i - 1]:
        count += 1

print(count)
