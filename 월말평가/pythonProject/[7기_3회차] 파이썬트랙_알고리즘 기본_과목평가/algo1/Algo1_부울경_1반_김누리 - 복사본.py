
#모든 행의 구간 합중 최대 값을 출력
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]
    lst = []
    for i in range(N):
        sum = 0
        for j in range(i,i+K):
            if j >= N:
                K -= 1
                continue
            else:
                sum += arr[i][j]
        lst.append(sum)

    mmax = 0
    for i in lst:
        if mmax < i:
            mmax = i
    print(f'#{tc} {mmax}')


