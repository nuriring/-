import sys
sys.stdin = open('5209.txt')

def DFS(i,ssum):
    global minV

    if ssum>minV: #가지치기
        return
    if i==N:
        # print(use)
        #if minV>ssum: # 이미 위에서 가지치기로 ssum이 minV보다 작은 경우만 살려두기 때문에 이 부분은 없어도됨
        minV=ssum
        return

    else:
        for j in range(N): #사용하지 않은 열들을 찾아서 순열로 만들어줌
            if visited[j] == 0: #아직 사용하지 않은 열이라면
                # use[i] = j #사용
                visited[j] = 1 #방문표시
                DFS(i+1,ssum+Arr[i][j]) #행 이동
                visited[j] = 0 #원상복귀


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cnt = 0
    visited = [0]*N
    use = [0]*N
    Arr = [list(map(int,input().split())) for _ in range(N)]
    minV = 123456789
    DFS(0,0)
    print(f'#{tc} {minV}')