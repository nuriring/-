import sys
sys.stdin = open('1249.txt')

def bfs(x,y):
    q = []
    q.append((x,y))
    visited = [[10000]*N for _ in range(N)]
    visited[x][y] = arr[x][y]

    while q:
        cx,cy = q.pop(0)
        for dx,dy in ((0,1),(1,0),(0,-1),(-1,0)):
            nx = cx+dx
            ny = cy+dy
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] > visited[cx][cy]+arr[cx][cy]:
                visited[nx][ny] = visited[cx][cy] + arr[cx][cy]
                q.append((nx,ny))
    return visited[N-1][N-1]

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]

    print(f'#{tc} {bfs(0,0)}')