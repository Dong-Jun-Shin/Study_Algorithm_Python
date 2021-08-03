# 부품 찾기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for m_val in m_list:
    if m_val in n_list:
        print("YES", end=' ')
    else:
        print("NO", end=' ')
