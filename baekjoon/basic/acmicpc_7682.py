# 틱택토
from collections import Counter


def win_check(char, board):
    # 가로
    for i in range(3):
        cnt = 0
        for j in range(3):
            if char == board[i][j]:
                cnt += 1
        if cnt == 3:
            return True

    # 세로
    for i in range(3):
        cnt = 0
        for j in range(3):
            if char == board[j][i]:
                cnt += 1
        if cnt == 3:
            return True

    # 대각선
    cnt = 0
    for i in range(3):
        if char == board[i][i]:
            cnt += 1
    if cnt == 3:
        return True

    cnt = 0
    for i in range(2, -1, -1):
        if char == board[i][2 - i]:
            cnt += 1
    if cnt == 3:
        return True

    return False


result = []
while True:
    string = input()
    if string == "end":
        break
    chars_cnt = Counter(string)
    board = []
    for i in range(0, 9, 3):
        board.append(string[i:i + 3])

    O_bool = win_check("O", board)
    X_bool = win_check("X", board)
    if O_bool and X_bool:
        result.append("invalid")
        continue

    if not(O_bool or X_bool) and chars_cnt["."] != 0:
        result.append("invalid")
        continue

    if O_bool:
        if chars_cnt["O"] == chars_cnt["X"]:
            result.append("valid")
        else:
            result.append("invalid")
    else:
        if chars_cnt["O"] + 1 == chars_cnt["X"]:
            result.append("valid")
        else:
            result.append("invalid")

[print(answer) for answer in result]

# O가 이겼을 때는
# len(X) == len(O)
# X가 이겼을 때, .이 없을 때
# len(X) == len(O) + 1
# 가로 세로 대각선
