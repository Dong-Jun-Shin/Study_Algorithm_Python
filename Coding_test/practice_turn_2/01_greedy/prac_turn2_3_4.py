# 1이 될 때까지
n, k = map(int, input().split())

result = 0
while n > 1:
    result += n % k
    result += 1
    n //= k

print(result)
