import sys
sys.stdin = open('2105.txt')

def DFS(n,ci,cj,v,cnt):
    global si,sj,ans
    ##가지치기
    if n==2 and ans>=cnt*2: #여태까지 얻은만큼 디저트를 먹어도 정답갱신 못함 # 사각형 모양이 두변만 정해지면 나머지 경로는 정해지니까
        return
    if n>3: #사각형 모양을 충족못함 종료조건 시계방향이 아닌 다른방향으로 회전해버리는 경우
        return
    #정답 갱신
    if n==3 and ci==si and cj==sj and ans<cnt: #정답갱신
        ans = cnt
        return

    for k in range(n,n+2):
        ni,nj = ci+di[k],cj+dj[k]
        if 0<=ni<N and 0<=nj<N and arr[ni][nj] not in v:
            DFS(k, ni, nj, v+[arr[ni][nj]], cnt+1)





di,dj = (1,1,-1,-1,1),(-1,1,1,-1,-1) #4방향에 더해서 하나를 더 해줘야(아무거나 상관없음 더미라고 불림) 다음 범위가 넘어가는 방향인지 조회가능하도록 브레이크를 걸어주기 위해 다섯개
#다섯개로 안하면 인덱스 에러남
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = -1 #디저트를 하나도 못먹엇을때
    for si in range(N):
        for sj in range(N):
            DFS(0,si,sj,[],0)
    print(f'#{tc} {ans}')
