# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # password 길이 계산
    len_pw = 0
    for i in password:
        len_pw += 1

    # 길이가 해당 범위를 만족하면 True, 아니면 False 반환
    if 8<= len_pw <=32:
        return True
    else: 
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
