import sys
sys.stdin = open('5205.txt')
def partition(s,e):
    lp = s+1 #left position
    rp = e #right position 은 end
    p = s #피봇은 start
    while lp<=rp: #같거나 교차되지 않는동안 반복
        while lp<=e and lst[p] >= lst[lp] : #lp가 내부에 위치하고, 피봇위치의 값보다 lp 값이 작은동안(같은 수 정렬 시 같다도 한쪽에 포함)
            lp += 1 #왼쪽에서 오른쪽으로 이동
        while rp>=s and lst[p] < lst[rp]: #rp가 내부에 위치하고, 피봇위치의 값보다 rp 값이 큰 동안
            rp -= 1 #오른쪽에서 왼쪽으로 이동
        if lp<rp: #while 문을 빠져나왔고 lp와 rp가 교차되지 않았으면
            lst[lp], lst[rp] = lst[rp],lst[lp] #swap
    lst[p],lst[rp] = lst[rp],lst[p] #lp,rp 교차 시 피봇위치 설정, 피봇보다 작은값인 rp와 교환해줘야 피봇을 기준으로 좌측이 작은값
    return rp
def qsort(s,e):
    if s<e: #길이가 최소한 1개이상은 되야함
        pivot = partition(s,e)  #[3개의데이터] < 12 < [5개의데이터]
        qsort(s,pivot-1)
        qsort(pivot+1,e)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    qsort(0,N-1)
    print(f'#{tc} {lst[N//2]}')