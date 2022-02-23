import sys
sys.stdin = open('algo1_sample_in.txt')

#모든 행의 구간 합중 최대 값을 출력
T = int(input())
for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split()))for _ in range(N)]


    mmax = 0
    for i in range(N):
        sol = 0
        for j in range(i,i+K):
            if j<N:
                sol += arr[i][j]
            else:
                break
        if mmax < sol:
            mmax = sol
    print(mmax)



