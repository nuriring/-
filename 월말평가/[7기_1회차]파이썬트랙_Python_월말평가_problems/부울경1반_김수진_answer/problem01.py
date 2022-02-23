# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def total(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 초기값 설정
    sum_value = 0
    # scores 리스트 내의 값들을 합산.
    for score in scores:
        sum_value += score
    return sum_value




# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(total(scores)) # 330
    