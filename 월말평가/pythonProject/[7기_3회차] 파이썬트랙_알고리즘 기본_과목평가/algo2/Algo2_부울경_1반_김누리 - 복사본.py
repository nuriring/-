
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]


    #4 방향 원소의 합
    di = [0,1,0,-1]
    dj = [1,0,-1,0]

    lst = []
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0<=ni<N and 0<=nj<N:
                    sum += arr[ni][nj]

            lst.append(arr[i][j]+sum)


    # 3*3 배열 원소의 합
    for i in range(N):
        for j in range(N):
            sum2 = 0
            for ii in range(i,i+3):
                for jj in range(j,j+3):
                    if 0 <= ii < N and 0 <= jj < N:
                        sum2 += arr[ii][jj]
                    lst.append(sum2)

    mmax = 0
    for i in lst:
        if mmax < i:
            mmax = i
    print(f'#{tc} {mmax}')




