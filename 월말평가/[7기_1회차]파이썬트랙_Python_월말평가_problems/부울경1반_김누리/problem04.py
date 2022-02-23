# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def check_duplicate_id(target_username, username_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 타겟 유저네임은 문자열, #유저네임 리스트는 리스트로 구성되어있다
    # 만약, 신규생성아이디가기존아이디와중복된다면True 
    if target_username in username_list : 
        return True
    else: #아니라면False를반환
        return False

    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    target_username = 'jungssafy'
    username_list = ['kimssafy', 'jungssafy']
    print(check_duplicate_id(target_username, username_list)) # True
