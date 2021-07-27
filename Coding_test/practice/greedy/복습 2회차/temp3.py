# 문자열 뒤집기
str = input()

cnt = 0
start = str[0]
for val in str:
    if start == val:
        continue
    start = val
    if val != str[0]:   
        cnt += 1

print(cnt)