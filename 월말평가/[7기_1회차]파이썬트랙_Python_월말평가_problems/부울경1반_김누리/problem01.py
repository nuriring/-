# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def total(scores):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    # 전체 점수의 합을 저장할 결과값을 생성합니다.
    result = 0
    # 점수 리스트를 순회합니다
    for score in scores:
        #결과값에 각각의 점수를 합산합니다
        result += score
    return result
    

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(total(scores)) # 330
