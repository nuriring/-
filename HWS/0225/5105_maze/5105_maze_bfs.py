import sys
sys.stdin = open('input.txt')
def fstart(N): #출발점 찾기
    for r in range(N):
        for c in range(N):
            if maze[r][c] == 2:
                return r, c
    return -1,-1 #못 찾는다면

def bfs(i,j,N):
    visited = [[0]*N for _ in range(N)] #미로의 크기만큼 생성
    queue = [] #큐생성
    queue.append((i,j)) #시작점 인큐
    visited[i][j] = 1# 시작점 방문표시
    #큐가 비어있지 않으면 반복
    while queue:
        i,j = queue.pop(0) #디큐 하면서 확인

        if maze[i][j] == 3:#도착하면
            return visited[i][j] - 2 #출발 도착 칸 제외한 최소거리를 반환해야하므로 -2 #너비우선탐색이니까 먼저도착한것이 최소거리가 가능한거임

        for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:  #i,j에 인접한 칸에 대해 우하좌상 조사
            ni,nj = i+di, j+dj #주변 칸 좌표
            # 미로를 벗어나지 않고, 인접한 칸 중에서 벽이 아니라면,
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0: #벽이아닌곳으로 검색해야 도착점인 3도 인식하기 때문에
                #인큐
                queue.append((ni,nj))
                visited[ni][nj] = visited[i][j] + 1 #거리를 구해줘야 하므로 이동할때마다 1씩 더해주면 그게 이동한 최단 거리가 된다.
    #도착지를 찾지 못한 경우
    return 0

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]
    sti, stj = fstart(N)
    ans = bfs(sti,stj,N) #시작점과 크기정보가 있으면 bfs를 돌릴수 있을 것이다
    print(f'#{tc} {ans}')







# def fstart(N): #출발점 찾기
#     for r in range(N):
#         for c in range(N):
#             if maze[r][c] == 2:
#                 return r, c
#     return -1,-1 #못 찾는다면
#
# def bfs(i,j,N):
#     visited = [[0]*N for _ in range(N)] #미로의 크기만큼 생성
#     queue = [] #큐생성
#     queue.append((i,j)) #시작점 인큐
#     visited[i][j] = 1# 시작점 방문표시
#     #큐가 비어있지 않으면 반복
#     while queue:
#         i,j = queue.pop(0) #t <- 디큐
#
#         if maze[i][j] == 3:#visit(t) : t에서 할일 처리
#             return visited[i][j] - 2 #출발 도착 칸 제외한 최소거리를 반환해야하므로, #그냥 최솟값을 출력해라면 그냥 visited[i][j]
#
#         for di,dj in [[0,1],[1,0],[0,-1],[-1,0]]:  #i,j에 인접한 칸에 대해 우하좌상 조사
#             ni,nj = i+di, j+dj #주변 칸 좌표
#             # 미로를 벗어나지 않고, 인접한 칸 중에서 벽이 아니라면,
#             if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1 and visited[ni][nj]==0: #벽이아닌곳으로 검색해야 도착점인 3도 인식하기 때문에
#                 #인큐
#                 queue.append((ni,nj))
#                 visited[ni][nj] = visited[i][j] + 1 #거리를 구해줘야 하므로 이동할때마다 1씩 더해주면 그게 이동한 최단 거리가 된다.
#     #도착지를 찾지 못한 경우
#     return 0
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(map(int,input())) for _ in range(N)]
#     sti, stj = fstart(N)
#     ans = bfs(sti,stj,N) #시작점과 크기정보가 있으면 bfs를 돌릴수 있을 것이다
#     print(f'#{tc} {ans}')

