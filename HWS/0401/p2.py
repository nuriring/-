

def bfs(s):
    q = []
    q.append(s)
    visited[s] = 1
    while q:
        cs = q.pop(0)
        print(cs,end=" ")
        for ce in range(E):
            if adjG[cs][ce] ==1 and visited[ce] == 0:
                q.append(ce)
                visited[ce] = 1

V = 7
E = 8
visited = [0]*E
adjG = [[0]*E for _ in range(E)]
data = list(map(int,input().split()))
for i in range(E):
    n1,n2 = data[i*2], data[i*2+1]
    adjG[n1][n2] = 1
    adjG[n2][n1] = 1
bfs(1)