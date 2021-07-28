# 문자열 재정렬
string = input()
totalNum = 0
strList = []
for char in string:
    if ord(char) <= ord('9'):
        totalNum += int(char)
    else:
        strList.append(ord(char))
strList.sort()

for char in strList:
    print(chr(char), end='')
print(totalNum)
