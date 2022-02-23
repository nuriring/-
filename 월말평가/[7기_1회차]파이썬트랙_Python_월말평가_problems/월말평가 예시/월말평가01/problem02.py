import json
from operator import length_hint
from urllib.parse import _NetlocResultMixinStr


def over(scores):
    
    length = 0
    for score in scores:
        if score >=60:
            length +=1
    return length



    # 여기에 코드를 작성합니다.


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    scores = [30, 60, 90, 70]
    print(over(scores)) # 3
