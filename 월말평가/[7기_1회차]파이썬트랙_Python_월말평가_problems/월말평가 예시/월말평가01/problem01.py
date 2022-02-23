import json


def max_score(scores):
    
    # data에는 index값과 점수 값이 주어져 있음 인덱스로 점수에 접근해서
    
    # 반복문을 돌려 최고점을 반환해야함
        #인덱스 첫번째 값을 기준으로 잡고 비교대상이 이상일때마다 해당 값을 할당해주면서 계속비교
    result = scores[0]
    for score in scores:
        if result <= score:
            result = score 
    return result #return 좀 for문에 넣지마라라랑라라라라라라ㅏㄹ

        



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
