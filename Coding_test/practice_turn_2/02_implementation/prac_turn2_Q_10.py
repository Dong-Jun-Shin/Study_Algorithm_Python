# 자물쇠와 열쇠
def turn_key(key):
    len_k = len(key)
    new_key = []
    for x in range(len_k):
        row_list = []
        for y in range(len_k - 1, -1, -1):
             row_list.append(key[y][x])
        new_key.append(row_list)
    return new_key

def check(new_lock):
    len_l = len(new_lock) // 3
    for x in range(len_l, len_l * 2):
        for y in range(len_l, len_l * 2):
            if new_lock[x][y] != 1:
                return False
    return True

def try_open(new_lock, key, start, end):
    len_k = len(key)
    for x in range(len_k):
        for y in range(len_k):
            new_lock[start + x][end + y] += key[x][y]
    if check(new_lock):
        return True
    for x in range(len_k):
        for y in range(len_k):
            new_lock[start + x][end + y] -= key[x][y]
    return False

def solution(key, lock):
    answer = True
    len_k, len_l, len_nl = len(key), len(lock), len(lock) * 3
    new_lock = [[0] * (len_nl) for _ in range(len_nl)]
    for i in range(len_l):
        for j in range(len_l):
            new_lock[i + len_l][j + len_l] = lock[i][j]
    
    for _ in range(4):
        for i in range(len_nl - len_k):
            for j in range(len_nl - len_k):
                if try_open(new_lock, key, i, j):
                    return True
        key = turn_key(key)

    return False


key	= [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
