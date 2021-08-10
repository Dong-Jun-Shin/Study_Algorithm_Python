# 곱하기 혹은 더하기
string = input()

result = 0
for char in string:
    char = int(char)
    if char == 0 or char == 1 or result == 0:
        result += char
    else:
        result *= char
    
print(result)
