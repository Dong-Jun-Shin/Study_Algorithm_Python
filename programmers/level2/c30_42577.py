# 전화번호 목록
# dictionary(Hash)를 활용해서, 비교할 리스트를 생성
# temp에 번호를 하나씩 추가하며 dictionary와 비교
def solution(phone_book):
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ''
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                return False
    return True


# str.startswith, .endswith(인자, idx) : 문자열의 앞이나 뒤에서 idx부터 인자가 일치하는지 확인
# str.find로 idx를 찾을 수 있음
# sort()와 startswith를 활용
# def solution(phone_book):
#     phone_book.sort()
#     target = phone_book[0]
#     for i in range(1, len(phone_book)):
#         if phone_book[i].startswith(target):
#             return False
#         else:
#             target = phone_book[i]
#     return True
