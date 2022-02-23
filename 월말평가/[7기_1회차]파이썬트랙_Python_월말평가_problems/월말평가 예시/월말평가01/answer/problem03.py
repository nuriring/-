import json


def menu_count(restorant):
    pass
    # 여기에 코드를 작성합니다.
    # 넘겨 받는 데이터 타입 확인하기.
    # print(restorant)
    # 그 중에서 필요한 정보
    # 메뉴 리스트...
    # dict에서 특정 value를 확인하는 방법
    # 1. [key] -> 대괄호에 key 넣어서 확인하기
    # print(restorant['menus'])
    # 2. dict.get(key) -> get 함수 사용해서 확인하기
    # print(restorant.get('menus'))

    # 메뉴들의 개수를 세야한다...
    # 최종 제출 변수
    result = 0 
    # 메뉴스 리스트만 순회
    # restorant이 가지고 있는 'menus' 키의 값
    # 리스트들 순회...
    for menu in restorant['menus']: # ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
        # 개수 하나당 result += 1
        result += 1
    # 최종 제출
    return result

    # 물론, 문제에서 built-in function 사용하면 안된다고 한적 없으니까
    # return len(restorant['menus'])


    # 자 그럼 여기서 문제.
    # [], get 왜 2개지?
    # 만약에 없는 키를 대괄호에 넣어보자.
    # print(restorant['age']) # -> KeyError: 'age'
    # 그 dict key 'age'가 없다. 오류 발생
    # print(restorant.get('age')) # -> None
    # dict.get() 도 get() 함수다!!
    # get() 함수 호출할때 넘겨준 인자 'age'에 해당하는 값이 없을때 None 반환
    # 그럼... 오류가 안나는 get()이 최강이다? 아니겠죠?
    # 상황에 따라서는 내가 원하는 값이 없을때, 코드가 멈춰야 할 수도 있다.
    # 오류가 안나고 다음 코드로 넘어가면 안될 수도 있다.
    # 혹은, 오류를 발생시키고, 그 상황에 대한 처리를 할 수 도 있다. -> error 파트에서 다룸.

    

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    restorant = {
        "id": 11,
        "user_rating": 5.5,
        "name": "김밥나라",
        "menus": ["참치김밥", "치즈라면", "돈까스", "비빔밥"],
        "location": "서울특별시 강남구 역삼동 123-123"
    }
    print(menu_count(restorant)) # 4
