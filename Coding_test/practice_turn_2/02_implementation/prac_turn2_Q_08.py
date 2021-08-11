# 문자열 재정렬
import bisect

s = list(input())
s.sort()
idx = bisect.bisect_left(s, 'A')
num = 0
for i in range(idx):
    num += int(s[i])

string = ""
for char in s[idx:]:
    string += char

string += str(num)
print(string)

""" Test case
K1KA5CB7
AJKDLSI412K4JSJ9D
"""
