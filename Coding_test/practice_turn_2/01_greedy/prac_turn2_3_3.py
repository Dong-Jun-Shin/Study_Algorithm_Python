# 숫자 카드 게임
n, m = map(int, input().split())
min_n_list = []
for _ in range(n):
    m_list = list(map(int, input().split()))
    min_n_list.append(min(m_list))

print(max(min_n_list))
