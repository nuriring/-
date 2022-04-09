import sys
sys.stdin = open('2819.txt')

di = [0,1,0,-1]
dj = [1,0,-1,0]

def DFS(n,ci,cj,num):
    if n==7:
        sset.add(num)
        return
    for k in range(4):
        ni,nj = ci+di[k], cj+dj[k]
        if 0<= ni<4 and 0<=nj<4:
            DFS(n+1,ni,nj,num*10+arr[ni][nj])

T = int(input())
for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
    # print(arr)
    sset = set()
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    print(f'#{tc} {len(sset)}')




