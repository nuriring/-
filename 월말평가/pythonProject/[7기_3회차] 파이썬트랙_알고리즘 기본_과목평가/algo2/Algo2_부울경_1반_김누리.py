import sys
sys.stdin = open('algo2_sample_in.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    #자기자신, 4 방향 4개, 3*3
    di = [0,0,1,0,-1,-1,-1,+1,+1]
    dj = [0,1,0,-1,0,-1,+1,+1,-1]


    #3*3
    mmax = 0
    for i in range(N):
        for j in range(N):
            ssum = 0
            for k in range(9):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    ssum += arr[ni][nj]
                else: #범위를 벗어나면 sum 초기화
                    ssum = 0
            if mmax < ssum:
                mmax = ssum


    # 4방향 배열 원소의 합
    for i in range(N):
        for j in range(N):
            ssum = 0
            for k in range(5):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    ssum += arr[ni][nj]
            if mmax < ssum:
                mmax = ssum
    print(mmax)





