# 베스트앨범
def solution(genres, plays):
    answer = []
    genre_dict = {genre:[] for genre in set(genres)}
    for i in range(len(genres)):
        genre_dict[genres[i]].append((plays[i], i))

    genre_list = []
    for genre in genre_dict:
        genre_list.append((sum([play for play, i in genre_dict[genre]]), genre))
    genre_list.sort(reverse=True)
    
    for play, genre in genre_list:
        answer += sorted(genre_dict[genre], key=lambda x:(-x[0], x[1]))[:2]

    answer = [i for play, i in answer]
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 800, 800, 2500]))
print(solution(["classic", "pop", "pop"], [600, 300, 2500]))
