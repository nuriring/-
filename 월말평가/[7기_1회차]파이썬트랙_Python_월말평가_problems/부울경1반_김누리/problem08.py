# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    
    # 인벤토리는 리스트 형태
    # item_type weapon에 해당하는 새로운 딕셔너리를 추가할 빈 리스트를 만든다
    result = []
    # 인벤토리의 리스트 내부에 접근한다
    for inven in inventory:
        if inven['type'] == 'weapon': # item 정보 딕셔너리에서 타입이 weapon일 때 조건을 달아준다
            result.append(inven) #type이 weapon일때 딕셔너리를 빈 리스트에 추가해준다

    return result
        
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
