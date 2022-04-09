di = [0,1,0,-1]
dj = [1,0,-1,0]
def fStart(N):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                sti,stj=i,j
                return sti,stj

def BFS(sti,stj):
    q = []
    q.append((sti,stj)) #시작점넣기
    visited[sti][stj] = 1 #방문표시
    while q:
        si,sj = q.pop(0)
        if arr[si][sj] == 3: #도착했다는 의미
            return visited[si][sj]-2
        for k in range(4):
            ni = si+di[k]
            nj = sj+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] ==0:
                q.append((ni,nj))
                visited[ni][nj] = visited[si][sj] + 1
    return 0


def DFS(sti,stj):
    stack = []
    stack.append((sti,stj)) #시작점넣기
    visited[sti][stj] = 1 #방문표시
    while stack:
        si,sj = stack.pop()
        if arr[si][sj] == 3: #도착했다는 의미
            return visited[si][sj]-2
        for k in range(4):
            ni = si+di[k]
            nj = sj+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] ==0:
                stack.append((ni,nj))
                visited[ni][nj] = visited[si][sj] + 1
    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # tc = input()
    arr = [list(map(int,input())) for _ in range(N)]
    # print(arr)
    visited = [[0]*(N) for _ in range(N)]
    sti,stj = fStart(N)
    # print(f'#{tc} {BFS(sti,stj)}')
    print(f'#{tc} {DFS(sti,stj)}')