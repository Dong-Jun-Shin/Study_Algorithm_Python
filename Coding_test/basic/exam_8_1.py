# x 받기
x = int(input())

# 연산에 필요한 횟수를 저장하는 dp 테이블 생성
dp = [0 for _ in range(x + 1)]

# 출력된 리스트 값의 인덱스 표시
print("[0", end='')
for i in range(1, x + 1):
    print(f'{i:3}', end='')
print("]")
print("-" * (2 + (3 * x) + 1))

# 1로 만드는 것이라, 0과 1은 배제
# 0부터 값에 필요한 연산 횟수 체크
for i in range(2, x + 1):
    # 1을 빼면 필요한 연산 횟수
    dp[i] = dp[i - 1] + 1

    # 이미 나누어 떨어진 값이 최소 몇번의 연산을 필요로 하는지 활용
    # 2로 나누어 떨어질 때, 필요한 연산 횟수
    if i % 2 == 0:
        # 1을 뺐을 때 필요한 횟수와 2로 나누었을 때 횟수를 비교해서 더 적은 연산값을 삽입
        dp[i] = min(dp[i], dp[i // 2] + 1)
    # 3로 나누어 떨어질 때, 필요한 연산 횟수
    if i % 3 == 0:
        # -1과 /2 중 더 적은 값과 /3 했을 때를 비교해서 더 적은 연산값을 삽입
        dp[i] = min(dp[i], dp[i // 3] + 1)
    if i % 5 == 0:
        # -1과 /2, /3 중 더 적은 값과 /5 했을 때를 비교해서 더 적은 연산값을 삽입
        dp[i] = min(dp[i], dp[i // 5] + 1)

# 필요한 최소 연산 횟수 출력
print(dp[x])
