# 문자열 뒤집기
string = input()
temp = ''
zero_cnt = 0
one_cnt = 0
for char in string:
    if temp == char:
        continue
    temp = char
    if temp == '0':
        zero_cnt += 1
    else:
        one_cnt += 1
    
print(min(zero_cnt, one_cnt))
