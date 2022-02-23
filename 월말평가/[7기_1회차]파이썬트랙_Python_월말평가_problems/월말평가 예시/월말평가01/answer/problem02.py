import json


def over(scores):
    pass
    # 여기에 코드를 작성합니다.
    # 최종 제출 답안
    result = 0
    # 전체 순회
    for score in scores:
        # 만약 score가 60점 이상 이라면
        if score >= 60:
            # result를 1 더해준다.
            # result = result + 1
            result += 1
    # 전부 순회하고, 전부 비교해서 다 끝나고 난 다음
    # 최종 제출
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
