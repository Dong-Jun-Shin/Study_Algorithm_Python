# N-Queen
# 배열 3개를 이용해서 현재 놓을 수 있는 행과 열의 여부를 판단
# 대각선 식은 row, col로 대각선마다 같은 값을 주는 식
def dfs(row):
    global answer, n

    if row == n:
        answer += 1
        return

    for col in range(n):
        # 세로축 중복확인 or 대각선(+) 중복 확인 or 대각선(-) 중복 확인
        if not(col_bool[col] or p_diag[row + col] or m_diag[row - col + n - 1]):
            col_bool[col] = p_diag[row + col] = m_diag[row - col + n - 1] = True
            dfs(row + 1)
            col_bool[col] = p_diag[row + col] = m_diag[row - col + n - 1] = False


n = int(input())
answer = 0
col_bool, p_diag, m_diag = [False] * n, [False] * (n * 2 - 1), [False] * (n * 2 - 1)
dfs(0)

print(answer)
