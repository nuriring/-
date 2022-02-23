# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.


def get_final_position(N, mat, moves):
    move_value = [(-1,0),(+1,0),(0,-1),(0,+1)]
    
    # 현재 위치 찾기
    for i in range(N):
        for j in range(N):
            if mat[i][j] == 1:
                x = i
                y = j
                break
    #이동 위치 찾기``
    for i in moves:
        x += move_value[i][0]
        y += move_value[i][1]
        # 한 턴에서 이동후 범위를 벗어나면 none반환
        if not (0<=x<N and 0<=y<N):
            return None
    return [x,y]

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    N = 3
    mat = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ] 
    moves1 = [1, 1, 3]
    print(get_final_position(N, mat, moves1)) # [2, 1]
    
    moves2 = [1, 3, 3]
    print(get_final_position(N, mat, moves2)) # [1, 2]