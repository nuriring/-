import sys
sys.stdin = open('4871.txt')
from pprint import pprint

# def dfs(v):
#     visited[v] = 1 #방문했다면 True표시
#     for w in range(1, V+1): #노드갯수만큼 반복 #오름차순으로 검색하는것과 같은 의미
#         if data[v][w] == 1 and visited[w] == 0: #길이있고 방문하지 않았다면
#             dfs(w) #w가 다시 v가 된다
#
# T = int(input())
# for tc in range(1,T+1):
#     V,E = map(int,input().split()) #V는 노드의 개수 E는 간선의 개수 #노드번호는1번부터
#     data = [[0]*(V+1) for _ in range(V+1)] #길을 기록할 이차원 배열
#     for _ in range(E):
#         s,e = map(int,input().split()) #s는 출발 노드 e 도착노드
#         data[s][e] = 1 #길을 기록
#     # pprint(visited)
#     check_s,check_e = map(int,input().split()) #경로가 있으면 1 없으면 0
#
#     visited = [0]*(V+1) #방문했는지를 기록할 1차원 배열 모두 False로 초기화
#
#     dfs(check_s) #출발점에서 깊이탐색 시작작
#
#     #다 조사한뒤 확인할 도착점의 visited 가 1 이라면 경로가 있다는 것을 의미
#     print(f'#{tc} {visited[check_e]}')


###1을 리턴해주는 방식으로 풀려면 재귀로 도착했다는 사실을 계속 리턴해줘야함
def DFS(s):
    visited[s] = 1
    if s == e: #출발점과 도착점이같으면
         return 1
    else:
        for ce in range(1,V+1): #연결된 정점 중에서 방문하지 않은 곳이 있다면
            if adjG[s][ce] == 1 and visited[ce] == 0:
                is_arrive = DFS(ce)
                if is_arrive:
                    return 1
    return 0

T = int(input())
for tc in range(1,T+1):
    V,M = map(int,input().split()) #V는 노드의 개수 E는 간선의 개수
    adjG = [[0]*(V+1) for _ in range(V+1)]
    visited = [0]*(V+1)
    for _ in range(M):
        i,j = list(map(int,input().split()))
        adjG[i][j] = 1
    s,e = map(int,input().split()) #검사해야할 출발 도착
    print(DFS(s))




