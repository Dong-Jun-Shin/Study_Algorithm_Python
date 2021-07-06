# find(), index() 함수로 문자열 검색하기

s1 = input('텍스트를 입력하세요.: ')    # 텍스트용 문자열
s2 = input('패턴을 입력하세요.: ')      # 패턴용 문자열

# 문자열 s1 ~ s2를 find()로 검색 (없을 경우, -1을 반환)
fIdx = s1.find(s2)
if fIdx == -1:
    print(f'fIdx: {fIdx}, 찾는 문자가 없습니다.')
else:
    print(f'{(fIdx + 1)}번째 문자가 일치합니다.')

# 문자열 s1 ~ s2를 index()로 검색 (없을 경우, ValueError를 반환)
try:
    iIdx = s1.index(s2)
    print(f'{(iIdx + 1)}번째 문자가 일치합니다.')
except ValueError:
    print(f'ValueError, 찾는 문자가 없습니다.')
