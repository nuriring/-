def is_id_valid(user_data):
    # user data의 id 값에 접근해서 마지막 값을 할당한다
    a = user_data['id'][-1]
 
    # 오류 사항 느낌표가 문자열이기 때문에 숫자와 비교가 안되므로
    # 문자열과 문자열을 비교하기 위해 문자열 리스트를 만든다.
    # numbers = ['0','1','2','3','4','5','6','7','8','9']

    # if a in numbers:
    #     return True
    # else:
    #     return False

    numbers = '0123456789'# 문자열도 시퀀스 기 때문에 가능
    if a in numbers:
        return True
    else:
        return False



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    user_data1 = {
        'id': 'jungssafy5',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data1)) 
    # True
    
    user_data2 = {
        'id': 'kimssafy!',
        'password': '1q2w3e4r',
    }
    print(is_id_valid(user_data2)) 
    # False