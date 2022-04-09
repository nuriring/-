import sys
sys.stdin = open('4615.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0]*(N+1) for _ in range(N+1)]
    arr[N//2][N//2] = arr[N//2+1][N//2+1] = 2 #초기 백돌놓기
    arr[N//2+1][N//2] = arr[N//2][N//2+1] = 1 #초기 흑돌놓기

    for _ in range(M):
        si,sj,d = map(int,input().split())

        arr[si][sj] = d
        for di,dj in ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1),(0,1)): #상3개 하3개 좌우 2개 총 여덟방향
            s = []
            for k in range(1,N): #오셀로 전체를 조회
                ni,nj = si+di*k,sj+dj*k
                if 1<=ni<=N and 1<=nj<=N: #범위 내에 존재하고
                    if arr[ni][nj] == 0: #비어있으면
                        break
                    elif arr[ni][nj] == d: #내 돌과 같으면
                        for ci,cj in s: #비어있지 않으면서 내돌과 다를 때 담아둔 좌표 들을 내 돌과 똑같이 바꿔줌
                            arr[ci][cj] = d
                        break
                    else:  #비어있지 않으면서 내돌과 다를 때 좌표들을 담아줌
                        s.append((ni,nj))
                else:
                    break

    #모두 수행 후 arr내의 흑돌 백돌 갯수세기
    bcnt = wcnt = 0
    for lst in arr:
        bcnt += lst.count(1)
        wcnt += lst.count(2)
    print(f'#{tc} {bcnt} {wcnt}')