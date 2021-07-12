# Nqueen 문제 알고리즘 구현하기
# 그림으로 출력


def make_arr(n: int) -> None:
    global pos, flag_row, flag_up_diagonal, flag_down_diagonal
    
    pos = [0] * n                                   # 각 열에 배치한 퀸의 위치
    flag_row = [False] * n                          # 각 행에 퀸을 배치했는지 체크
    flag_up_diagonal = [False] * (n * 2 - 1)        # 대각선 방향(↙↗)으로 퀸을 배치했는지 체크
    flag_down_diagonal = [False] * (n * 2 - 1)      # 대각선 방향(↘↖)으로 퀸을 배치했는지 체크


def put() -> None:
    """퀸의 위치를 □와 ■로 출력 (행 단위 출력)"""
    for j in range(n):
        for i in range(n):
            print('■ ' if pos[i] == j else '□ ', end='')
        print()
    print()


def set(i: int) -> None:
    """i열의 알맞은 위치에 퀸을 배치"""
    for j in range(n):
        if(not flag_row[j]                                    # 각 행에 퀸이 배치되지 않고
            and not flag_up_diagonal[i + j]                   # 대각선 방향(↙↗)으로 퀸이 배치되지 않고
            and not flag_down_diagonal[i - j + (n - 1)]):     # 대각선 방향(↘↖)으로 퀸이 배치되지 않았다면
            pos[i] = j                                        # 퀸을 j행에 배치
            if i == (n - 1):                                  # 모든 열에 퀸을 배치 완료
                put()
            else:
                flag_row[j] = flag_up_diagonal[i + j] = flag_down_diagonal[i - j + (n - 1)] = True
                set(i + 1)                              # 다음 열에 퀸을 배치
                flag_row[j] = flag_up_diagonal[i + j] = flag_down_diagonal[i - j + (n - 1)] = False


n = int(input('정배열의 크기를 입력해주세요.: '))
make_arr(n)
set(0)      # 0열에 퀸을 배치
