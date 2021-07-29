# 자물쇠와 열쇠
# 0 0 0   1 1 1
# 1 0 0   1 1 0
# 0 1 1   1 0 1

def turn_90_degree(array):
    turnArray = [[] for _ in range(len(array[0]))]
    for j in range(len(array[0])):
        for i in range(len(array) - 1, -1, -1):
            turnArray[j].append(array[i][j])
    return turnArray

def check(newLock):
    lenLock = len(newLock) // 3
    # 확인
    for x in range(lenLock, lenLock * 2):
        for y in range(lenLock, lenLock * 2):
            if newLock[x][y] != 1:
                return False
    return True

def solution(key, lock):
    # 1. lock을 세배 크기로 만든 후, 가운데로 집어넣기
    lenLock = len(lock)
    lenKey = len(key)
    newLock = [[0] * (lenLock * 3) for _ in range(lenLock * 3)]
    for i in range(lenLock):
        for j in range(lenLock):
            newLock[i + lenLock][j + lenLock] = lock[i][j]

    for rotation in range(0, 4):
        # 2. 세배 크기의 lock에 key를 하나씩 대입하며 화인
        for i in range(lenLock * 2):
            for j in range(lenLock * 2):
                # 열쇠 매치
                for x in range(lenKey):
                    for y in range(lenKey):
                        newLock[i + x][j + y] += key[x][y]
                # 확인
                if check(newLock) == True:
                    return True
                # 열쇠 빼기
                for x in range(lenKey):
                    for y in range(lenKey):
                        newLock[i + x][j + y] -= key[x][y]
        # 3. 회전
        key = turn_90_degree(key)

    # 2 ~ 4 반복하면서, 매치가 되면 True 리턴, 4번 돌렸을 때 매치가 안되면 False 리턴
    return False



key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key, lock))
