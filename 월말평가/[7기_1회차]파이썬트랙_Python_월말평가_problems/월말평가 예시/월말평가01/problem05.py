def is_user_data_valid(user_data):
    if user_data['id']== '' or user_data['password'] == '':
        return False
    else:
        return True
    
    # 여기에 코드를 작성합니다.
# 아이디와 비밀 번호 모두 빈 값이 입력되는 것을 방지
# user_data가 딕셔너리 형태로 들어온다고 할 때,
# 사용자가 입력한 아이디와 비밀번호 중 하나라도 '비어있는 문자열' 이면 False
# 아니라면 True 를 반환하는 함수를 완성


# 반대로
# 만약에 id가 빈문자열이 "아니고", password "도" 빈문자열이 아니면,
# if user_data['id'] != '' and user_data['password'] != '':
#     return True
# else:
#     return False
#  두 코드 모두 가능

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': '',
        'password': 'sdfsefe',
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