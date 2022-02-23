def is_user_data_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    # print(user_data)
    # 만약에 id, password "둘중에 하나라도" 비어있는 문자열이면
    # False 반환하고 종료
    # if user_data['id'] == '':
    #     return False
    # elif user_data['password'] == '':
    #     return False
    # # 아니먄
    # else:
    #     return True

    # 위에 처럼만 적어도 정답 맞습니다.
    # 근데 우리 모처럼 파이썬 배우고 있는데..
    # 코드 한번 바꿔봅시다.
    # 만약에, id가 빈 문자열 "이거나" password가 빈문자열 이면
    # if user_data['id'] == '' or user_data['password'] == '':
    #     return False
    # else:
    #     return True
    
    # 반대로
    # 만약에 id가 빈문자열이 "아니고", password "도" 빈문자열이 아니면,
    if user_data['id'] != '' and user_data['password'] != '':
        return True
    else:
        return False

    # 위 코드 3개 다 정답입니다.
    # 정답일지 궁금하다면...
    # 아래의 코드는 수정하지 않습니다. 라고 되어있지만.....
    # 제출할때만 원래대로 돌려놓고 제출하시면 됩니다...
    # 그래서 다양한 상황 만들어보고 제출해 주세요...


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data1)) 
    # False 

    user_data2 = {
        'id': 'jungssafy',
        'password': '1q2w3e4r',
    }
    print(is_user_data_valid(user_data2)) 
    # True

    # 위에 있는 값들은 건들지 말고...
    # 밑에 새로운 테스트 케이스 만들어서 테스트 하고 지우기...
    # user_data3 = {
    #     'id': '',
    #     'password': '',
    # }
    # print(is_user_data_valid(user_data3)) 
    # # False
    # 그래도 위 코드를 혹시나 잘못 건드릴것 같다면...
    # 파일을 따로 복사해서 테스트하고,,,
    # 답만 잘 제출하자....