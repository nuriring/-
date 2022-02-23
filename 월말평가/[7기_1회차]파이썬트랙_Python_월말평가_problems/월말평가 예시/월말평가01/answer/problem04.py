import json


def turn(temperatures):
    pass
    # 여기에 코드를 작성합니다.
    # 최종 제출 변수 만들기
    # 비어있는 딕셔너리... result = {}
    # 어??? {} 이거 세튼데...? 하면 혼나요
    # 세트는 {} <- 이걸로 비어있는 세트 못만들어요
    # 그럼 왜 dict() 말고 {}로 만들었느냐...? 는 조금있다가 보죠 ^^;
    # '맥시멈', '미니멈' 키와 벨류가 없다보니
    # 리스트에 값추가하려다가 keyerror 발생했다... 
    # 처음 딕셔너리 만들때부터 값 만들어주고 가자....
    result = {
        'maximum': [],
        'minimum': []
    }
    # 전체 순회
    for temp in temperatures:
        # 리스트를 순회 했는데... 또 리스트가 나왔다...
        # print(temp)
        # 또 순회... 해야할까?
        # 상황에 따라 다르다...
        # 우리가 해야 할 일
        # 두 기온중에, 높은 온도를 maximum에 집어넣고
        # 낮은 온도는 minimum에 집어 넣을 것이다...
        # 즉, 두 기온을 비교할 수만 있으면 된다...
        # temp 리스트의 0번째와 1번째를 비교한다...
        # 0번째 요소가 1번째 요소보다 크다면?
        if temp[0] >= temp[1]:
            # result가 가진 'maximum'키의 벨류에 0번째를 추가
            # 리스트에 값 추가하기?
            # 1. list.append() 함수 사용하기
            result['maximum'].append(temp[0]) # keyerror ???
            # result에 maximum 이라는 키 없어요. 지금...
            # 그럼 어떻게 하지?
            # 처음 result 만들때...... 'maximum' 이라는 키에 해당하는
            # 비어있는 리스트 만들어주자......
            # 2. list + list
            result['minimum'] += [temp[1]]
        # 반대는?
        else:
            # 위에 넣은거랑 반대로 넣기
            result['maximum'].append(temp[1])
            result['minimum'] += [temp[0]]
    # 전부 반복하고 나서
    # 딕셔너리 출력 결과가 순서가 예시랑 다르다...
    # 문제 없음 -> 딕셔너리는 순서를 보장하지 않는다.
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    temperatures = [
        [9, 3],
        [9, 0],
        [11, -3],
        [11, 1],
        [8, -3],
        [7, -3],
        [-4, -12]
    ]
    print(turn(temperatures)) 
    # {
    #     'maximum': [9, 9, 11, 11, 8, 7, -4], 
    #     'minimum': [3, 0, -3, 1, -3, -3, -12]
    # }
