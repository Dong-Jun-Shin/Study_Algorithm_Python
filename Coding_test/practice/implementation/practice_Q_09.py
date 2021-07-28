# 문자열 압축
def solution(s):
    # 압축할 수 없을 때, 문자열 길이이므로 문자열 길이로 설정
    answer = len(s)
    # 문자 단위 1개부터 절반까지(len(s)//2 + 1)
    # (길이 8->인덱스 5가 나와야 4까지 묶어서 판별)
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:0 + step]
        # 현재 선택한 문자열 단위 개수 1
        count = 1
        # 문자 단위 개수부터, 문자 단위 수만큼 증가
        for i in range(step, len(s), step):
            # 리스트에 범위 지정할 때, 리스트 길이를 초과하면 리스트 길이만큼만 나옴
            if prev == s[i:i + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                count = 1
                prev = s[i:i + step]
        # count만 하고 나왔을 때, 남아있는 문자열 삽입
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))

    return answer

s = "ababcdcdababcdcd"
print(solution(s))
