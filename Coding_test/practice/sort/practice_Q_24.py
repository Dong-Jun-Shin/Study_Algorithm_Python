# 안테나
n = int(input())
location_home = list(map(int, input().split()))
location_home.sort()

print(location_home[(n - 1) // 2])
