# 보이어'무어법으로 문자열 검색하기

def bm_match(txt: str, pat: str) -> int:
    """보이어'무어법으로 문자열 검색"""
    skip = [None] * 256                 # 건너뛰기 표

    # 건너뛰기 표 만들기
    for pt in range(256):
        skip[pt] = len(pat)             # 건너뛰기 표를 패턴 길이만큼 설정
    for pt in range(len(pat)):
        # pt번째 패턴 문자의 유니코드를 코드 포인트로 바꾸고, 해당 코드 포인트를 위치로 하는 건너뛰기 표에 건너뛸 거리를 삽입
        # (현재 문자에서 패턴 끝까지의 거리 > 패턴 길이 - pt 번째 - 1)
        skip[ord(pat[pt])] = len(pat) - pt - 1
    # 건너뛰기 표가 다 만들어진 후, pt는 (패턴 길이 - 1)인 3이 되어있음

    # 검색하기
    while pt < len(txt):                # 텍스트의 커서가 모두 스캔할 때까지
        pp = len(pat) - 1               # 패턴의 끝을 커서에 삽입
        while txt[pt] == pat[pp]:       # 텍스트 끝과 패턴의 끝을 비교
            if pp == 0:                 # 패턴의 첫문자까지 같으면
                return pt               # 텍스트에서 일치하는 첫 인덱스를 반환
            pt -= 1                     # 일치하기 때문에, 현재 텍스트 커서에서 하나 이전 문자에 커서를 주목
            pp -= 1                     # 일치하기 때문에, 현재 패턴 커서에서 하나 이전 문자에 커서를 주목
        # 일치하는 문자가 없기 때문에, 
        # 현재 건너뛸 거리가 1보다 작으면, 1이 추가되도록 설정
        # len(pat) - pp = len(pat) - (len(pat) - 1) = 1
        pt += skip[ord(txt[pt])] if skip[ord(txt[pt])] > len(pat) - pp else len(pat) - pp  

    return -1


if __name__ == '__main__':
    s1 = input('텍스트를 입력하세요.: ')    # 텍스트용 문자열
    s2 = input('패턴을 입력하세요.: ')      # 패턴용 문자열

    idx = bm_match(s1, s2)                 # 문자열 s1 ~ s2를 보이어'무어법으로 검색

    if idx == -1:
        print('텍스트 안에 패턴이 존재하지 않습니다.')
    else:
        print(f'{(idx + 1)}번째 문자가 일치합니다.')
