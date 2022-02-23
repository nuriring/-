import json


def turn(temperatures):
    # # 기온 리스트 내부를 순회한다
    # max_list = []
    # min_list = []
    # for temperature in temperatures:
    #     #print(temperature
    #     # max값에는 최고기온을 min 값에는 최저기온을 할당한다
    #     max = temperature[0]
    #     #print(max)
    #     min = temperature[1]
    #     # 새로운 리스트를 생성한다
    #     max_list += [max]
    #     min_list += [min]
    #     # 위의 리스트를 값으로 가지는 새로운 딕셔너리를 생성한다
    #     new_dict={'maximum': max_list, 
    #                 'minimum' : min_list
    #     }
    # return (new_dict)
    
# 두 기온중 높은 값이 뭔지 모른다면
# 먼저 비어있는 리스트를 값으로 가지는 새로운 딕셔너리를 만들어주고 이후에 append 해줍니다
    result = {'maximum':[], 'minimum' : []}
# 전체 순회
    for temp in temperatures:
        if temp[0] >= temp[1]:
            # result가 가진 maximun키의 벨류에 0번째를 추가
            # 리스트에 값 추가
            result['maximum'].append(temp[0])
            result['minimum'].append(temp[1])
        else : 
            result['maximum'].append(temp(1))
            result['minimum'].append(temp[0])
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
