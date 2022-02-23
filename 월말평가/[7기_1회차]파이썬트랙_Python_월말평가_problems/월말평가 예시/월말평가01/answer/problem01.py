import json


def max_score(scores):
    # 여기에 코드를 작성합니다.
    # 왠만해선 모든것들을 프린트를 찍고 출력 결과를 알아보자,
    # print(scores)
    # 우리는 리스트를 순회해서 그 리스트가 가진 값들중에
    # 제일 크거나 작은 값을 찾을 것이다.
    # 그 말은... 비교대상은... 항상 리스트 안에 있는 값들로만 찾을 것이다.
    # 리스트의 가장 첫번째 값을 초기 값으로 두고
    # 비교해 나간다면... 어떤 수를 기초 값으로 잡아도 비교할때 문제 없다.
    # 리스트는 인덱스 접근 가능 -> 첫번째 요소의 인덱스는 0
    # 최종 반환할 결과
    result = scores[0]
    # 잘 넣어졌나? print(result)
    # 전체 요소 순회하기...
    for score in scores:
        # print(score)
        # 순회해서 가져온 각 값들과
        # 최종 제출할 답안이랑 비교하기
        # 제일 큰거 찾을 거다.
        # 지금 설정한 result보다 순회중인 score가 더 크다면...
        # 최종 제출할 값은 score에 들어 있는 값이 될 테니...
        # result에 담아놓은 값을 score에 있는 값으로 바꾸기.
        if result <= score:
            result = score
    # scores가 가진 요소 순회가 다 끝났다
    # for문이 끝났다.
    # for문이 끝난건? 띄어쓰기를 기준으로 판단
    # 답 제출
    return result



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(max_score(scores)) # 90
