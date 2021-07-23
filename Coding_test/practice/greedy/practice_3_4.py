# 1이 될 때까지
n, k = map(int, input().split())

count = 0
while n >= k:
    count += n % k
    n //= k
    count += 1

count += (n - 1)
print(count)
