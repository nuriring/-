def is_id_valid(user_data):
    pass
    # 여기에 코드를 작성합니다.
    # 만약에 id의 마지막 글자가.......
    # 마지막 글자? 글자 -> 문자열 -> 순서가 있다 -> index 접근 -> 마지막? -> -1
    # if user_data['id'][-1] ??? # 누구랑 비교하는가......
    # 가 떠오르지 않을때는... 우선은... 하나하나 비교해 봅시다.
    # True가 반환될 상황을 만들어 봅시다.

    # jungssafy5 -> 마지막이 0~9 안에 있는 숫자다.. 예를 가지고 테스트 해보자.
    # if user_data['id'][-1] == 5: # None이 나온다.... 왜지....?
    #     return True
    # print(type(user_data['id'][-1])) # 아... 문자열이구나...

    # 문자열이랑 문자열 비교하기..
    # if user_data['id'][-1] == '5': 
    #     return True
    # # 자 그러면 이제 우리가 할 일은...
    # if user_data['id'][-1] == '0': 
    #     return True
    # if user_data['id'][-1] == '1': 
    #     return True
    # if user_data['id'][-1] == '2': 
    #     return True
    # if user_data['id'][-1] == '3': 
    #     return True
    # 한다고 문제 될게 있을까?
    # 0~9까지 다 적어서 내어도 코드만 맞다면 문제 X
    # 그러니 어렵다고 포기 말기...

    # 이걸 조금 스맛흐 하게 풀어보자...
    # 어떻게하면 좋을까?
    
    # 1. 0~9 ? range?
    # 도전
    # if user_data['id'][-1] ..... range(10)... 무언가랑 같다면....
    # in 연산자...?
    # 그리고 비교할 아이디의 마지막 -1을 숫자로 바꾸기
    # if int(user_data['id'][-1]) in range(10):
    #     return True
    # 오.. 처음에는 맞음...
    # 문제는 마지막 글자가 숫자가 아니면 int로 형 변환 안됨......
    # 느낌표 ! 는 int로 형변환 할 수 없음....??
    
    # 그럼... 그냥 문자열이랑 비교하자
    # 아래와 같이 작성 가능
    # numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    # if user_data['id'][-1] in numbers:
    #     return True
    # else:
    #     return False
    # 답 잘 나옴...

    # 조금더 똑똑하게 해볼까?
    # in 연산자 sequence에 쓸 수 있다.
    # 문자열도 시퀀스이다.
    numbers = '0123456789'
    if user_data['id'][-1] in numbers:
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