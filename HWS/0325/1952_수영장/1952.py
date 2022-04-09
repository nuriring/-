import sys
sys.stdin = open('input.txt')
def DFS(n,ssum):
    global ans #ans는 넘겨줘도 되지만 참조하면 디버깅에 도움이 됨
    if n>12:
        if ans>ssum:
            ans=ssum
        return
    #일일권
    DFS(n+1, ssum+lst[n]*day)
    #월간
    DFS(n+1, ssum+mon)
    #분기
    DFS(n+3, ssum+mon3)
    #년간
    DFS(n+12, ssum+year)


T = int(input())
for tc in range(1,T+1):
    day, mon, mon3, year = map(int,input().split())
    lst = [0] + list(map(int,input().split()))
    ans = 12345678
    DFS(1,0)
    print(f'#{tc} {ans}')


    ##dp
    D = [0]*13
    for i in range(1,13):
        mmin = D[i-1] + lst[i]*day
        mmin = min(mmin,D[i-1]+mon)
        if i>=3:
            mmin = min(mmin, D[i-3] + mon3)
        if i>=12:
            mmin = min(mmin, D[i-12] + year)
        D[i] = mmin
    print(f'#{tc} {D[12]}')