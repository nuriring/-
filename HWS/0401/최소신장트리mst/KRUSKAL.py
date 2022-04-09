def find_set(x):
    while x != rep[x]:
        x = rep[x]
    return x


def union(x, y):
    rep[find_set(y)] = find_set(x)


V, E = map(int, input().split())  # V 마지막 정점, 0~V번 정점, 개수(V+1)개
edge = []
for _ in range(E):
    u, v, w = map(int, input().split())  # 간선 연결 u-v 와 비용 w
    edge.append([w, v, u])
edge.sort()
print(edge)
rep = [i for i in range(V + 1)]  # 대표원소배열
# MST의 간선수 N = 정점수 -1 (V+1-1)
N = V + 1
cnt = 0  # 선택한 edge의 수
total = 0  # MST 가중치의 합

for w, v, u in edge:
    if find_set(v) != find_set(u):
        cnt += 1  # 그래프에 추가
        union(u, v)  # 사이클 발생시 제외해주기 위해 union 작업 필요
        total += w  # 비용 더하기
        if cnt == N - 1:  # V개가 되야하니까 간선수가 #MST 구성이 끝나면
            break
print(total)
