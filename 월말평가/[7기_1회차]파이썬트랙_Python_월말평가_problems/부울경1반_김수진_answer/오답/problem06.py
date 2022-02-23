# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def caesar(word, n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    result = ''

    # 각 문자의 변환값을 result에 추가
    for i in word:
        ord_num = ord(i)
        
        # 문자가 대문자일 때 (A:65)
        if 65<= ord_num <= 90:
            # A를 기준으로 얼만큼 더해야하는지 계산 
            # (범위를 넘어갈 경우를 고려하여 26으로 나눈 나머지로 계산)
            add_v = (n+ord_num-65)%26
            # 계산한 값만큼 더한 후 문자로 변환하여 result에 추가
            result += chr(65+ add_v)

        # 문자가 소문자일 때 (a:97)   
        else:
            add_v = (n+ord_num-97)%26
            result += chr(97+ add_v)
        
    return result


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(caesar('apple', 5))
    # fuuqj
    print(caesar('ssafy', 1))
    # ttbgz
    print(caesar('Python', 10))
    # Zidryx