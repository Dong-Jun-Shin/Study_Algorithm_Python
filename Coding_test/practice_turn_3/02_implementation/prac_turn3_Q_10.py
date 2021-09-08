# 자물쇠와 열쇠
def rotate_key(key):
    length_key = len(key)
    new_key = [[] for _ in range(length_key)]
    for j in range(length_key):
        for i in range(length_key - 1, -1, -1):
            new_key[j].append(key[i][j])
    return new_key


def check_key(key, new_lock):
    length_lock = len(new_lock) // 3
    for a in range(length_lock):
        for b in range(length_lock):
            if new_lock[length_lock + a][length_lock + b] != 1:
                return False
    return True


def try_open(key, new_lock, i, j):
    length_key = len(key)
    for a in range(length_key):
        for b in range(length_key):
            new_lock[a + i][b + j] += key[a][b]
    if check_key(key, new_lock):
        return True
    for a in range(length_key):
        for b in range(length_key):
            new_lock[a + i][b + j] -= key[a][b]
    return False


def solution(key, lock):
    length_lock = len(lock)
    new_lock = [[0] * (length_lock * 3) for _ in range(length_lock * 3)]
    for i in range(length_lock):
        for j in range(length_lock):
            new_lock[length_lock + i][length_lock + j] = lock[i][j]

    for _ in range(4):
        for i in range(length_lock * 2 + 1):
            for j in range(length_lock * 2 + 1):
                if try_open(key, new_lock, i, j):
                    return True
        key = rotate_key(key)

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
