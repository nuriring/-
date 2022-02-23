# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.

    # 결과값과 리스트 길이 초기값 설정
    sum_value = 0
    len_score = 0

    #scores 리스트를 회문하면서 합산과 길이를 구함.
    for i in scores:
        sum_value += i
        len_score += 1

    # 평균 = 합/갯수
    return sum_value/len_score


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores)) # 82.5
    