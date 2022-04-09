import sys
sys.stdin = open('5189.txt')

def DFS(i):
    global result,ssum

    if i==N-1:
        # print(use) #첫번째 시작점과 도착점은 1 이니까 사이에 경로만 순열로 경우의 수를 먼저 만들어줌
        ssum = arr[1][use[0]] + arr[use[-1]][1] #사무실에서 출발할때와 사무실에서 복귀할때는 따로 더해서 초기화해줌
        idx = 0
        while idx < len(use)-1:
            ssum += arr[use[idx]][use[idx+1]] #사이의 경로를 순열로 만들어주고 거기에 해당하는 배터리 값을 더해줌
            idx +=1
        if result>ssum: #최소값으로 갱신
            result = ssum
            return


    else:
        for j in range(N-1): #사용하지 않은 열들을 찾아서 순열로 만들어줌
            if visited[j] == 0: #아직 사용하지 않은 열이라면
                use[i] = A[j] #사용
                visited[j] = 1 #방문표시
                DFS(i+1) #행 이동
                visited[j] = 0 #원상복귀




T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [[0]*(N+1)]+[[0]+list(map(int,input().split())) for _ in range(N)]
    visited = [0]*(N-1)
    # visited = [[0]*(N+1) for _ in range(N+1)]
    use = [0]*(N-1)
    A = [x for x in range(2,N+1)]
    # print(A)
    result = 12345678
    ssum = 0
    DFS(0)
    print(f'#{tc} {result}')


