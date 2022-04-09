import sys
sys.stdin = open('1219.txt')
####dfs - recur 버전
def dfs(n):
    visited[n] = 1
    for w in range(0, 100):
        if G[n][w] == 1 and visited[w] == 0:
            dfs(w)

for tc in range(1,11):
    tc,E = map(int,input().split()) #E는 길의 갯수
    visited = [0] * 100
    data = list(map(int,input().split()))
    G = [[0]*100 for _ in range(100)] #길을 기록할 이차원 배열 노드는 0에서 99까지
    for i in range(0,len(data),2):
        G[data[i]][data[i+1]] = 1

    dfs(0) #출발점에서 깊이탐색 시작작

    #다 조사한뒤 확인할 도착점의 visited 가 1 이라면 경로가 있다는 것을 의미
    print(f'#{tc} {visited[99]}')


##############DFS - stack버전
def DFS(s):
    stack = []
    stack.append(s)
    visited[s] = 1
    while stack:
        cs = stack.pop()
        for ce in range(100):
            if adjG[cs][ce] == 1 and visited[ce] == 0:
                stack.append(ce)
                visited[ce] = 1

for _ in range(10):
    adjG = [[0]*100 for _ in range(100)]
    tc,M = map(int,input().split()) #tc와 M은 간선의 개수
    data = list(map(int,input().split()))
    visited = [0]*100
    for i in range(M):
        adjG[data[i*2]][data[i*2+1]] = 1

    # print(adjG[6])
    DFS(0) #0에서 출발해서 99에 도착할 수 있는지
    print(f'#{tc} {visited[99]}')



###############BFS 버전
def BFS(s):
    q = []
    q.append(s) #시작점 넣기
    visited[s] = 1 #시작점 방문체크
    while q:
        cs = q.pop(0) #출발점 pop
        for ce in range(100):
            if adjG[cs][ce] ==1 and visited[ce] == 0 : #길이있고 방문하지 않았다면
                q.append(ce) #방문
                visited[ce] = 1 #방문표시

for _ in range(10):
    adjG = [[0]*100 for _ in range(100)]
    tc,M = map(int,input().split()) #tc와 M은 간선의 개수
    data = list(map(int,input().split()))
    visited = [0]*100
    for i in range(M):
        adjG[data[i*2]][data[i*2+1]] = 1

    # print(adjG[6])
    BFS(0) #0에서 출발해서 99에 도착할 수 있는지
    print(f'#{tc} {visited[99]}')







# def dfs(n): #인덱스번호 1부터 고려버전
#     visited[n] = 1
#     for w in range(1, 101):
#         if G[n][w] == 1 and visited[w] == 0:
#             dfs(w)
#
# for _ in range(10):
#     tc, E = map(int, input().split())
#     data = list(map(int, input().split()))
#     visited = [0] * 101
#     G = [[0 for _ in range(101)] for _ in range(101)]
#     for i in range(0, len(data), 2):
#         G[data[i]][data[i+1]] = 1
#     dfs(0)
#     print(f'#{tc} {visited[99]}')





