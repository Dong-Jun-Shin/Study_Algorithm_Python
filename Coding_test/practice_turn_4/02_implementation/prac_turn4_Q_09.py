# 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        new_s = ''
        cmp_cnt = 1
        cmp_char = s[:i]
        for j in range(i, len(s), i):
            if s[j:j + i] == cmp_char:
                cmp_cnt += 1
                continue
            if cmp_cnt != 1:
                new_s += str(cmp_cnt)
                cmp_cnt = 1
            new_s += cmp_char
            cmp_char = s[j:j + i]
        if cmp_cnt != 1:
            new_s += str(cmp_cnt)
            cmp_cnt = 1
        new_s += cmp_char
        cmp_char = s[j:j + i]
        answer = min(answer, len(new_s))
    return answer

s = "ababcdcdababcdcd"
print(solution(s))
