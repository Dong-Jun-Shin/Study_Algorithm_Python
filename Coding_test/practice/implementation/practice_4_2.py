# 왕실의 나이트
codi = input()
move = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

codi = [ord(codi[0]), int(codi[1])]
result = 0
for case in move:
        x = codi[0] + case[0]
        y = codi[1] + case[1]
        if (ord('a') <= x and x < ord('i')) and (1 <= y and y < 9):
            result += 1

print(result)
