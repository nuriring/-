import json


def menu_count(restorant):
    
    # key값을 통해 restorant 딕셔너리의 menus항목에 접근한다
    # 해당 value의 list 내부를 순회한다
    result = 0
    for menus in restorant['menus']:
        #print(menus)
        result += 1
    return result

    # 여기에 코드를 작성합니다.
    

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
