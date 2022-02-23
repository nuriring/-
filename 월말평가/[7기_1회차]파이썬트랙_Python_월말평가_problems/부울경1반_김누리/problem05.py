# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_password_length(password):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 전달되는 비밀번호는 문자열
    # 비밀번호는최소8자이며, 최대32자이다 -> 조건
    # 입력된정보가해당범위를만족한다면True, 아니라면False를반환

    # password 문자열의 길이를 저장할 값을 초기화해줍니다
    length = 0
    # password 문자열을 순회합니다
    for word in password:
        length += 1 #1씩 추가합니다
    # 비밀번호 길이에 조건을 달아 줍니다
    if 8 <= length <=32:
        return True
    else:
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    password = 'q1w2e3r4'
    print(check_password_length(password)) # True
