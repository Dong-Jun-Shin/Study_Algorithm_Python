# 문자열 뒤집기
strList = list(map(int, input()))

count = 0
for i in range(1, len(strList)):
    # 현재 문자열과 시작 문자열이 다르고 이전 문자열과도 다르면 카운트
    if strList[i] != strList[0] and strList[i] != strList[i - 1]:
        count += 1

print(count)
