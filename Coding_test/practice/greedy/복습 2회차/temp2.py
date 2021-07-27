# 곱하기 혹은 더하기
str = input()

result = 0
for val in str:
    val = int(val)
    if val <= 1 or result == 0:
        result += val
    else:
        result *= val

print(result)
