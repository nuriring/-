import sys
sys.stdin = open('4875.txt')

def check(nx, ny): #이동 가능 여부 확인
    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]==1: #범위를 벗어나지 않고 벽이라면
        # 못간다
        return False
    return True #그 외에는 갈 수 있다

dx = [0,1,0,-1] #우하좌상
dy = [1,0,-1,0]


def dfs(x,y):
    for k in range(4):
        nx = x+dx[k]
        ny = y+dy[k]
        #경계조건
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == 3: #한번이라도 도착했다면#함수 끝내기
                return 1 #return으로 도착햇다는 사실 메아리로 알리기
            else: #아직도착못했다면
                if check(nx,ny): #이동가능하다면
                    arr[nx][ny] = 1 #방문 표시, 따로 배열을 안만들어주는 이유는 한번 갔던 길은 이미 유망성이 낮기 때문
                    is_arrive = dfs(nx,ny) #다음 위치로 이동 #재귀호출 사용
                    arr[x][y] = 0
                    if is_arrive: #재귀호출 값이 도착했다는 1이라면
                        return 1
    return 0#dfs를 다 수행했는데 return1에 걸리지 못했다는 것은 막힌 미로라는 것을 의미

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]


    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                result = dfs(i,j)
                #깊이 탐색 시작할 출발점
                break
    print(f'#{tc} {result}')



