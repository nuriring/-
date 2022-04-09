import sys
sys.stdin = open('input.txt')

# 탐색 시작점v
def BFS(v):
    # 방문 가능 지점 = 정점의 개수
    visited = [0]*(V+1)
    queue = []
    # 탐색 시작점
    queue.append(v)
    # 작업할 일이 남아 있는 동안
    while queue: #큐가 비어있지 않은 동안
        # print(queue, end=' ')
        # queue의 첫 번째 원소 반환
        v = queue.pop(0)
        # 방문 하지 않았다면,
        if not visited[v]:
            visited[v] = True
            #visit(v) 정점 v에서 할일
            print('{} {}'.format(v, visited))
            for w in range(1, V+1): #v와 연결된 모든 w에 대해서
                if G[v][w] == 1 and visited[w] == 0: #w까지 가는길이 있고 방문한적이 없다면
                    queue.append(w) #큐에 추가


V, E = map(int, input().split()) #노드의 범위 1~7까지, E는 간선의 갯수
data = list(map(int, input().split())) #간선 정보

G = [[0 for _ in range(V + 1)] for _ in range(V + 1)] # 길정보 표시할 그리드

for i in range(V + 1):
    '''
    G[data[0]][data[1]] = 1
    G[data[1]][data[0]] = 1

    G[data[2]][data[3]] = 1
    G[data[3]][data[2]] = 1
    '''
    G[data[i * 2]][data[i * 2 + 1]] = 1 #방향성이 없으므로 양쪽다 번갈아가면서 그리드에 길표시
    G[data[i * 2 + 1]][data[i * 2]] = 1

BFS(1)