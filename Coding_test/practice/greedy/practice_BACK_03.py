# ATM
n = int(input())
p = list(map(int, input().split()))

result = 0

p.sort()

for i in range(len(p)):
    for j in range(i + 1):
        result += p[j]

print(result)
