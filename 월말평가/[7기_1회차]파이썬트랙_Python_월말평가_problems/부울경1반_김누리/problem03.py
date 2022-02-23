# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def get_user_id(data):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # get_user_id함수에는파이썬의딕셔너리(dictionary) 형태로신규생성을목표하는정보(user_data)가전달인자
    # 입력된정보에서아이디(id)를문자열형태로반환하는get_user_id함수
    
    # 문자열 형태로 반환하기 위해 빈 문자열을 저장합니다
    result = ''
    # user_data의 id 값에 접근해서 빈 문자열에 추가합니다
    result += data['id']
    return result

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    user_data = {
        "id": "jungssafy",
        "password": "q1w2e3r4",
        "password_confirm": "q1w2e3r4"
    }
    print(get_user_id(user_data)) # 'jungssafy'
