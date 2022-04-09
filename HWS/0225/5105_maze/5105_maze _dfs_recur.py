import sys
sys.stdin = open('input.txt')
def fstart(N): #출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
    return -1,-1 #못찾는다면 어쩔건데

###미로를 벗어나는 범위 설정을 안할려면 0으로 미로를 패딩해줘도 된다
### bfs 출구만 찾고 끝내기또는 최단거리 구하는 경우 bfs 가 dfs보다유용
##또한 bfs 는 출발지가 여러개여도 된다


##dfs 재귀로 풀어보자
def dfs(i,j,N,c): #c 지나온 칸수
    global minV
    if maze[i][j]==3: #목적지에 도착하면 기존의 최소거리와 비교
        if minV > c:
            minV = c
        return
    elif c>minV: #이미 최소거리보다 커버리면 그만 , 너무 많이 왔는데?? 가지치기
        return

    else:
        maze[i][j] = 1 #갔던길 또 가지 않도록 벽으로 만들어줌 #이거는 델타탐색 중복 방지를 위해서
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni,nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and maze[ni][nj]!=1:
                dfs(ni,nj,N,c+1) #한 칸이동
        maze[i][j] = 0 #다시 파면서 돌아가기 visited로 해도 다시 파면서 돌아가는건 똑같음 그래서 굳이 미로만한 애를 만들 이유는 없음
        # 이거는 또 다른 길로 가는 출구가 있을지도 모르니까 걔를 탐색할 수 있게 만들어주기 위해서



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int,input())) for _ in range(N)]

    sti, stj = fstart(N)

    minV = 100000 # (N*N) 아무리커도 넘을 수 없음

    dfs(sti, stj, N, 0) #구하는 경로 범위에 따라 c값 조절
    if minV!=100000:
        print(f'#{tc} {minV-1}') #출발지는 빼줌
    else: #도착이 불가능하면 갱신이 불가능
        print(f'#{tc} 0')



