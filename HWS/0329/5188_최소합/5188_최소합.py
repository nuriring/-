

def DFS(i,j,n,ssum):
    global ans
    if ssum>ans:
        return
    if n == (N-1)*2:
        ans=ssum
        return
    for di,dj in ((0,1),(1,0)):
        ni = i+di
        nj = j+dj
        if 0<=ni<N and 0<=nj<N:
            DFS(ni,nj,n+1,ssum+arr[ni][nj])





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    ans = 123456789
    DFS(0,0,0,arr[0][0]) #출발
    print(f'#{tc} {ans}')


###################################################################


def DFS(i,j,n,ssum):
    global ans
    if ssum>ans:
        return
    if n == (N-1)*2:
        ans=ssum
        return
    for di,dj in ((0,1),(1,0)):
        ni = i+di
        nj = j+dj
        if 0<=ni<N and 0<=nj<N:
            DFS(ni,nj,n+1,ssum+arr[ni][nj])





T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)
    ans = 123456789
    DFS(0,0,0,arr[0][0]) #출발
    print(f'#{tc} {ans}')


