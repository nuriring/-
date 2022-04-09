import sys
sys.stdin = open('input.txt')
#탈주범은 시간당 1 움직일수 있음

di = [-1,1,0,0]
dj = [0,0,-1,1]
#pipe 정보 [상,하,좌,우]  [0,1,2,3]
pipe = [[0,0,0,0],
        [1,1,1,1],
        [1,1,0,0],
        [0,0,1,1],
        [1,0,0,1],
        [0,1,0,1],
        [0,1,1,0],
        [1,0,1,0]]
opp = [1,0,3,2] #상일때는 하, 하일때는 상, 좌일때는 우, 우일때는 좌 #룩업테이블 방식


def BFS(N,M,R,C,L):

    q = []

    q.append((R,C))
    v[R][C]=1
    cnt = 1 #start를 1로 시작

    while q:
        ci,cj = q.pop(0)
        # c += 1
        if v[ci][cj] == L:
             return cnt ##만약에 10시간 지나는걸 구하라는데 그 안에 파이프가 끊겨져있는 경우가 있으면 얘는 여기서 값을 리턴 못함 따라서 전체에 return 해줘야됨 마지막 줄에
        for k in range(4):
            ni,nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<M and v[ni][nj]==0 and pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]: #파이프와 이어진 파이프가 모두 연결되어 있따면
                q.append((ni,nj))
                v[ni][nj]=v[ci][cj]+1
                # s.append(arr[ni][nj])
                cnt+=1
    return cnt

T = int(input())
for i in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    #N세로크기 M가로크기 R세로위치 C가로위치 L탈출후소요시간
    arr = [list(map(int,input().split())) for _ in range(N)]
    v = [[0 for _ in range(M)] for _ in range(N) ]
    cnt = 0
    print(BFS(N,M,R,C,L))
    # print(arr)
    # print(v)
