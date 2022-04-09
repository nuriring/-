import sys
sys.stdin = open('input.txt')

###노드의 거리는 1차원 배열로 풀수있따???

def bfs(s,e):
    q=[]
    q.append(s)
    visited[s] = 1 #시작점 방문표시

    while q:
        cs = q.pop(0)
        if cs == e: #current start가 end 도착점과 같아지면
            return visited[cs]-1 #이때가지 거리를 return #출발점cnt는 제외해줌
        for ce in range(1,V+1):
            if adjG[cs][ce] == 1 and visited[ce] == 0: #current end가 방문하지 않은 지점이면,
                q.append(ce)
                visited[ce] = visited[cs] + 1
    return 0 #큐가 다 비워져도 못찾으면 0 리턴


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    adjG = [[0 for _ in range(V+1)] for _ in range(V+1)]
    # print(adjG)
    for _ in range(E):
        i,j = map(int,input().split())
        adjG[i][j] = 1
        adjG[j][i] = 1 #방향성이 없음
    s,e = map(int,input().split()) #출발,도착노드
    visited = [0]*(V+1)

    print(f'#{tc} {bfs(s,e)}')
