# 문자열 압축
def solution(s):
    answer = length = len(s)
    for i in range(1, length//2 + 1):
        new_str = ""
        compare_str = s[0:i]
        count = 1
        for j in range(i, length, i):
            if s[j:j + i] == compare_str:
                count += 1
                continue

            if count > 1:
                new_str += f"{count}{compare_str}"
            else:
                new_str += compare_str

            count = 1
            compare_str = s[j:j + i]
        else:
            if count > 1:
                new_str += f"{count}{compare_str}"
            else:
                new_str += compare_str
        answer = min(answer, len(new_str))
    return answer


s = "ababcdcdababcdcd"
print(solution(s))
