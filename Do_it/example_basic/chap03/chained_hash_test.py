# 체인법을 구현하는 해시 클래스 ChainedHash의 사용

from enum import Enum
from chained_hash import ChainedHash

Menu = Enum('Menu', ['추가', '삭제', '검색', '덤프', '종료'])    # Enum 'Menu' 타입의 [...]를 원소로 갖는 객체 선언


def select_menu() -> Menu:
    """메뉴 선택"""
    s = [f'({m.value}){m.name}' for m in Menu]    # for문을 이용해서 리스트 원소로 각각 추가

    while True:
        print(*s, sep='    ', end='')    # list에 있는 원소를 positional arguments 방식으로 전달해서 sep으로 구분지어 출력
        n = int(input(': '))
        if 1 <= n <= len(Menu):
            return Menu(n)


hash = ChainedHash(13)          # 크기가 13인 해시 테이블을 생성

while True:
    menu = select_menu()        # 메뉴 선택

    if menu == Menu.추가:       # 추가
        key = int(input('추가할 키를 입력하세요.: '))
        val = input('추가할 값을 입력하세요.: ')
        if not hash.add(key, val):
            print('추가를 실패했습니다!')

    elif menu == Menu.삭제:     # 삭제
        key = int(input('삭제할 키를 입력하세요.: '))
        if not hash.remove(key):
            print('삭제를 실패했습니다!')

    elif menu == Menu.검색:     # 검색
        key = int(input('검색할 키를 입력하세요.: '))
        t = hash.search(key)
        if t is not None:
            print(f'검색한 키를 갖는 값은 {t}입니다.')
        else:
            print('검색된 데이터가 없습니다.')

    elif menu == Menu.덤프:     # 덤프
        hash.dump()

    else:                       # 종료
        break
