import sys
sys.stdin = open('5251.txt')
def dijkstra(s,V): #s는 출발
    visited = [0]*(V+1)
    visited[s] = 1
    for i in range(V+1):
        D[i] = adjM[s][i]
        print(D[i]) #[0, 1, 6]
    for _ in range(V):#시작노드 제외 전체 노드에 대해 반복
        minV = INF
        w = 0
        for i in range(V+1):
            if visited[i] == 0 and minV > D[i]: #방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 찾는다
                minV = D[i]
                w = i
        visited[w] = 1 #방문표시
        for v in range(V+1):
            D[v] = min(D[v], D[w]+adjM[w][v]) #현재노드를 거쳐서 다른 노드로 이동하는 거리와 비교했을때 최솟값을 기록해놓는다
            print(D)

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #V는 마지막정점번호 #E는 간선갯수 #V+1은 정점갯수,
    INF = 10000 #이어져있지 않으면 무한대로 초기화
    adjM = [[INF]*(V+1) for _ in range(V+1)]
    for i in range(V+1):
        adjM[i][i] = 0 #자기자신에게 가는 경로는 0
    for _ in range(E):
        u,v,w = map(int,input().split()) #start, end, 비용
        adjM[u][v] = w
    print(adjM)

    D = [0]*(V+1) #0번에서 각 노드마다 최소 거리를 구해보자
    dijkstra(0,V)
    print(f'#{tc} {D[-1]}')