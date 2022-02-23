# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def dec_to_bin(n):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 종료 조건(n이 2보다 작을 때)
    if n < 2:
        return str(n)

    # 몫을 함수에 입력하고, 2로 나눈 나머지가 뒤에 붙여지도록 반환하도록 함
    return dec_to_bin(n//2) + str(n%2)




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(dec_to_bin(10))
    # 1010
    print(dec_to_bin(5))
    # 101
    print(dec_to_bin(50))
    # 110010