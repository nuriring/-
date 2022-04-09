import sys
sys.stdin = open('input.txt')

def BFS(s):
    q = []
    v = [0]*101
    q.append(s) #루프로 큐에집어넣는 여러개 형식이 될 수 있다.
    v[s] = 1 #방문표시
    sol = s #갱신을 위한 초기값

    while q:
        c = q.pop(0)
        if v[sol]<v[c] or v[sol]==v[c] and sol<c : #같을때는 sol<c일때
            sol = c
        for j in range(1,101):
            if adj[c][j]==1 and v[j]==0:
                q.append(j)
                v[j]=v[c]+1

    # return c #그냥 출력하면 10이 나오게 될것 우리는 17을 출력받아야함
    return sol
T = 1
for test_case in range(1,T+1):
    N, S = map(int,input().split())
    lst = list(map(int,input().split()))
    adj = [[0]*101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1
    ans = BFS(S)
    print(f'#{test_case} {ans}')