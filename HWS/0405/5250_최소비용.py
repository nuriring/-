import sys
sys.stdin = open('5250.txt')
from collections import deque


def bfs(i, j, h):
    q = deque()
    q.append((i, j, h)) #현재위치와 높이를 함께 넣어준다
    visited[i][j] = 0 #초기 비용은 0
    while q:
        ci, cj, ch = q.popleft()
        #if ci == N - 1 and cj == N - 1: #도착하면 return
            #return #안돼!! 멈춰!! 최솟값을 계속 갱신해주고 있기 때문에 도달하고 나서도 여러번 돌면서 더 나은 값을 찾으면 갱신할 수 있게해줘야됨

        for di, dj in ((0, 1), (1, 0), (0, -1), (-1, 0)): #상하좌우 이동
            ni = ci + di
            nj = cj + dj
            if 0 <= ni < N and 0 <= nj < N: #범위내에 있을때
                nh = arr[ni][nj] #현재 높이
                extra = nh - ch #높이차에 따른 연료 보급값
                if extra <= 0: #높이가 더 낮아져서 보급값이 - 가 되면
                    extra = 0 #추가 연료 필요 없음
                if visited[ni][nj] > visited[ci][cj] + extra + 1:
                    visited[ni][nj] = visited[ci][cj] + extra + 1
                    q.append((ni, nj, nh)) #이동 위치와 높이 큐에넣어줌


T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # N*N
    arr = [list(map(int, input().split())) for _ in range(N)]
    # print(arr)
    INF = 10000 #무제한으로 초기화
    visited = [[INF] * N for _ in range(N)]
    # print(visited)
    bfs(0, 0, arr[0][0])
    print(f'#{tc} {visited[N - 1][N - 1]}')
