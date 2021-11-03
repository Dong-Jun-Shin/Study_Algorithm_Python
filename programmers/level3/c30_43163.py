# 단어 변환
# yield 키워드를 사용하면 yield로 지정한 값으로 구성된 리스트를 함수가 반환
def check(begin, target):
    cnt = 0
    for i in range(len(begin)):
        if begin[i] != target[i]:
            cnt += 1
    return True if cnt == 1 else False

def dfs(begin, target, words, change, idx):
    answer = 50
    if begin == target:
        return idx
    if idx != len(words):
        for i in range(len(words)):
            if i not in change and check(begin, words[i]):
                change.append(i)
                answer = min(answer, dfs(words[i], target, words, change[:], idx + 1))
                change.remove(i)
    return answer

def solution(begin, target, words):
    if target not in words:
        return 0
    return dfs(begin, target, words, [], 0)


print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution(	"hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
