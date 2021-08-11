# 문자열 압축
def solution(s):
    answer = len(s)
    for i in range(1, len(s)//2 + 1):
        string = ''
        count = 0
        compare = s[:i]
        j = 0
        while j < len(s):
            if s[j:j + i] == compare:
                count += 1
            else:
                if count > 1:
                    string += str(count) + compare
                elif count == 1:
                    string += compare
                compare = s[j:j + i]
                count = 0
                continue
            j += i
        if count > 1:
            string += str(count) + compare
        elif count == 1:
            string += compare
        answer = min(answer, len(string))

    return answer


# abcabcdede
s = "abcabcdede"
print(solution(s))