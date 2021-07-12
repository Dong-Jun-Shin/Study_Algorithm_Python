# 행(j)과 열(i)에 퀸을 1개 배치하는 조합을 재귀적으로 나열하기 (행, 열 중복 고려)
# 열(i)=7, 행(j)=7까지 진행 후, 열(i)를 줄이면서 행(j)의 조합을 확인

pos = [0] * 8                   # 각 열에서 퀸의 위치
flag_row = [False] * 8              # 각 행에 퀸을 배치했는지 체크


def put() -> None:
    """각 열에 배치한 퀸의 위치를 출력"""
    for i in range(8):
        print(f'{pos[i]:2}', end='')
    print()


def set(i: int) -> None:
    """i열의 알맞은 위치에 퀸을 배치"""
    for j in range(8):
        if not flag_row[j]:         # j행에 퀸을 배치하지 않았으면
            pos[i] = j          # 모든 열에 퀸 배치를 완료
            if i == 7:
                put()
            else:
                flag_row[j] = True
                set(i + 1)      # 다음 열에 퀸을 배치
                flag_row[j] = False


set(0)                          # 0열에 퀸을 배치
