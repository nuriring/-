def dfs(s):
    visited[s] = 1
    print(s,end=" ")
    for e in range(E):
        if adjG[s][e] == 1 and visited[e] == 0:
            dfs(e)




V = 7
E = 8
visited = [0]*E
adjG = [[0]*E for _ in range(E)]
data = list(map(int,input().split()))
for i in range(E):
    n1,n2 = data[i*2], data[i*2+1]
    adjG[n1][n2] = 1
    adjG[n2][n1] = 1
# print(adjG)
dfs(1)