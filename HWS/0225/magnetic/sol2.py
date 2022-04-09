import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    # 1은 N극 2는 S극
    data = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    # 전체 N극, S극 개수 확인
    end = 0
    for i in range(n):
        for j in range(n):
            if data[i][j] == 1:
                end += 1
            if data[i][j] == 2:
                end += 1
    # 상, 하
    # -1, 1
    while end:
        for i in range(n):
            for j in range(n):
                # N극 자성체 -> 아래로만 이동
                if data[i][j] == 1:
                    # 벽 체크 -> 테이블을 벗어나면 사라짐
                    if n == i+1:
                        data[i][j] = 0
                        end -= 1
                    # s극 체크 -> s극과 n극 교착 상태로 변경, 교착상태 +1
                    elif data[i+1][j] == 2:
                        result += 1
                        data[i][j] = 3
                        data[i+1][j] = 3
                        end -= 2
                    # 이미 교착상태 -> 현재 위치 교착상태로만 변경
                    elif data[i+1][j] == 3:
                        data[i][j] = 3
                        end -= 1
                    # 아래가 같은 극 -> 대기
                    elif data[i+1][j] == 1:
                        continue
                    # 아무것도 아니면 -> 한칸 아래로 이동
                    else:
                        data[i][j] = 0
                        data[i+1][j] = 1
                # S극 -> 위로만 이동
                elif data[i][j] == 2:
                    # 벽 체크 -> 테이블을 벗어나면 사라짐
                    if 0 > i-1:
                        data[i][j] = 0
                        end -= 1
                    # n극 체크 -> s극과 n극 교착 상태로 변경, 교착상태 +1
                    elif data[i-1][j] == 1:
                        result += 1
                        data[i][j] = 3
                        data[i-1][j] = 3
                        end -= 2
                    # 이미 교착상태 -> 현재 위치 교착상태로만 변경
                    elif data[i-1][j] == 3:
                        data[i][j] = 3
                        end -= 1
                    # 위가 같은 극 -> 대기
                    elif data[i - 1][j] == 2:
                        continue
                    else:
                        data[i][j] = 0
                        data[i-1][j] = 2

    print(f'#{tc} {result}'.format(tc, result))