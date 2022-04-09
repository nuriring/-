import sys
sys.stdin = open('input.txt')

di = [0,1,0,-1]
dj = [1,0,-1,0]

def fstart(N): #출발점찾기
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i,j
def bfs(i,j,N):
    visited = [[0]*16 for _ in range(16)] #방문표시 미로크기만큼
    # print(visited)
    queue = []
    queue.append((i,j)) #시작점 인큐
    visited[i][j] = 1 #시작점 방문표시
    while queue: #큐가 비어있지 않으면 반복
        i,j = queue.pop(0)
        if arr[i][j] == 3: #도착하면 길이 있다는 거니까 1을 리턴
            return 1
        for k in range(4):
            ni = i+di[k]
            nj = j+dj[k]
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == 0:
                queue.append((ni,nj)) #미로를 벗어나지 않고 인접한 칸 중 벽이 아니고 방문하지 않았다면 인큐
                visited[ni][nj] = 1 #방문표시
    return 0 #도착점을 찾지못하고 큐가 빈 경우 길이 없으므로 0을 리턴

for _ in range(10):
    N = 16
    tc = int(input())
    arr = [list(map(int,input())) for _ in range(16)]
    # print(type(arr[0][0]))
    sti,stj = fstart(N)
    # print(sti,stj)
    res = bfs(sti,stj,N)
    print(f'#{tc} {bfs(sti,stj,N)}')
