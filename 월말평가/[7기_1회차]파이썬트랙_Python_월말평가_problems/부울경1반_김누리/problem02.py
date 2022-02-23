# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def average(scores):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    #1번에서 풀었던 전체 점수의 합산을 활용합니다
    result = 0
    for score in scores:
        result += score
    # 평균값은 전체 점수의 합산을 리스트 내부 값들의 개수의 합으로 나누어줍니다
    # 리스트 내부 값들의 갯수의 합을 할당할 변수를 만들어줍니다
    length = 0
    # 리스트를 순회합니다
    for score in scores:
        length += 1 # 순회할때마다 1씩 증가
    
    return result/length


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    scores = [80, 90, 85, 75]
    print(average(scores)) # 82.5
