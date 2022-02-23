# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    
    # M값에 따른 x와 y의 이동 값 저장
    move_value = [(-1,0),(1,0),(0,-1),(0,1)]

    # M값에 따른 이동 후 위치 계산
    x = position[0] + move_value[M][0]
    y = position[1] + move_value[M][1]

    # x와 y가 범위 내에 존재하면 True, 아니면 False 반환
    if 0<=x<N and 0<=y<N:
        return True
    else:
        return False


# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0))) # True
    print(is_position_safe(3, 0, (0, 0))) # False
