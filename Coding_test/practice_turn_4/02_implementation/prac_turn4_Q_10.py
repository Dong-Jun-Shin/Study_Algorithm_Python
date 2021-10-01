# 자물쇠와 열쇠
def rotate_key(key):
    len_key = len(key)
    new_key = [[0] * len_key for _ in range(len_key)]
    for i in range(len_key):
        for j in range(len_key):
            new_key[i][j] = key[(len_key - 1) - j][i]
    return new_key


def check_lock(new_lock):
    len_lock = len(new_lock) // 3
    for x in range(len_lock, len_lock * 2):
        for y in range(len_lock, len_lock * 2):
            if new_lock[x][y] == 1:
                continue
            return False
    return True


def try_open(new_lock, key, i, j):
    len_key = len(key)
    for x in range(len_key):
        for y in range(len_key):
            new_lock[x + i][y + j] += key[x][y]
    if check_lock(new_lock):
        return True
    for x in range(len_key):
        for y in range(len_key):
            new_lock[x + i][y + j] -= key[x][y]
    return False


def solution(key, lock):
    len_lock = len(lock)
    new_lock = [[0] * (len_lock * 3) for _ in range(len_lock * 3)]
    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[len_lock + i][len_lock + j] = lock[i][j]

    for _ in range(4):
        for i in range(len_lock * 2 + 1):
            for j in range(len_lock * 2 + 1):
                if try_open(new_lock, key, i, j):
                    return True
        key = rotate_key(key)
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
