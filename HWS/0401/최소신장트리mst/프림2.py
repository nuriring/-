#최솟값을 키값을 갱신하는 것 대신에 좀더 직접적으로 찾는 prim2

def prim2(r,V):
    MST = [0] * (V+1) #mst 포함 여부
    MST[r] = 1 #출발지 mst 표시
    s = 0 #최소 가중치의 합을 선택될때마다 기록해줄거임
    for _ in range(V): #1개는 미리 포함시켰으니까 V-1번 반복
        u = 0 #선택할 정점 번호
        minV = 10000
        for i in range(V+1):#extract min #MST에 포함된 정점i와 인접한 정점j 중
            if MST[i] == 1: #포함된 정점이 나오면
                for j in range(V+1): #나머지 정점에 대해서
                    if 0<adjM[i][j]<minV and MST[j]==0: #인접(무한대x,0도 아님)이고 and mst에 속하지 않은 정점중에서 값이 더 작을때만 갱신해 나감
                        u = j
                        minV = adjM[i][j]

        s += minV #최솟값을 더해줌
        MST[u] = 1 #MST에 방문했다고 추가
    return s


V,E = map(int,input().split()) #0번에서 V번까지 정점 #간선의갯수
adjM =  [[0]*(V+1) for _ in range(V+1)] #가중치를 기록할 인접행렬
#adjL = [[] for _ in range(V+1)] #인접리스트도 가능
for _ in range(E):
    u,v,w = map(int,input().split()) #정점 두개와 가중치 w
    adjM[u][v] = w
    adjM[v][u] = w
    #adjL[u].append((v,w)) #인접리스트도 가능
    #adjL[v].append((u,w))


print(prim2(0,V))