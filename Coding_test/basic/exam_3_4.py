"""------------------------------book
# n, k를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
result = 0

while True:
    # (n을 k로 나눈 몫에 k를 곱해서, n에 가장 가까운 k배수를 target에 삽입)
    target = (n // k) * k
    # n에서 target을 빼는 것은 뺄셈 횟수를 뜻하므로 result에 추가
    result += (n - target)
    # 뺄셈 연산을 고려했으니, 뺄셈이 적용된 값인 target을 n에 삽입
    n = target

    # 뺄셈 연산 후, 더 이상 나눌 수 없는지 판단
    if n < k:
        break

# 나눗셈 후, 남은 수에 대한 뺄셈 연산
result += (n - 1)
print(result)
----------------------------------"""
# ---------------------------------me
# n, k 받기
n, k = map(int, input().split())

cnt = 0
while n != 1:
    # 나눗셈 처리
    while n % k == 0:
        n //= k
        cnt += 1

    # 뺄셈 처리
    if n != 1:
        n -= 1
        cnt += 1

print(cnt)
# -----------------------------------
