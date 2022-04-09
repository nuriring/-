
def prim1(r,V):
    MST = [0]*(V+1) #MST 포함여부
    key = [10000]*(V+1) #가중치의 최대값 이상으로 초기화. key[v]는 v가 MST에 속한 정점과 연결될 때의 가중치
    key[r] = 0 #시작정점의 KEY
    for _ in range(V): #V+1개의 정점 중 V개를 선택
        #MST에 포함되지 않은 정점 중 (MST[u]==0), key가 최소인 u찾기
        u =  0 #시작점이 0일때만 가능한 초기화값
        minV = 10000 #extract min
        for i in range(V+1):
            if MST[i]==0 and minV>key[i]: #mst에 속하지 않았고 무한대가아니니까 인접하면서, 가장 최소거리의 인덱스를 찾아감
                u=i
                minV=key[i]
        MST[u] = 1 #정점 u를 MST에 추가
        #u에 인접인 v에 대해, mst에 포함되지 않은 정점이면
        for v in range(V+1):
            if MST[v] == 0 and adjM[u][v] > 0:
                key[v] = min(key[v], adjM[u][v]) #u를 통해 MST에 포함되는 비용과 기존 비용을 비교후 갱신

    return sum(key) #MST 가중치의 합



V,E = map(int,input().split()) #0번에서 V번까지 정점 #간선의갯수
adjM =  [[0]*(V+1) for _ in range(V+1)] #가중치를 기록할 인접행렬
#adjL = [[] for _ in range(V+1)] #인접리스트도 가능
for _ in range(E):
    u,v,w = map(int,input().split()) #정점 두개와 가중치 w
    adjM[u][v] = w
    adjM[v][u] = w
    #adjL[u].append((v,w)) #인접리스트도 가능
    #adjL[v].append((u,w))


print(prim1(0,V))