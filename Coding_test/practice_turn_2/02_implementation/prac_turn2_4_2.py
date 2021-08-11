# 왕실의 나이트
codi = input()

x = ord(codi[0])
y = int(codi[1])

d1 = [-2, 2]
d2 = [1, -1]

result = 0
for d_x in d1:
    for d_y in d2:
        nx = x + d_x
        ny = y + d_y
        if ord('a') <= nx <= ord('h') and 1 <= ny <= 8:
            result += 1

for d_x in d2:
    for d_y in d1:
        nx = x + d_x
        ny = y + d_y
        if ord('a') <= nx <= ord('h') and 1 <= ny <= 8:
            result += 1

print(result)
