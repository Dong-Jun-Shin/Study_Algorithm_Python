# 큰 수의 법칙
n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))

n_list.sort(reverse=True)

cycle = n_list[0] * k + n_list[1]
share = m // (k + 1)
remainder = m % (k + 1)

result = cycle * share + n_list[0] * remainder
print(result)
