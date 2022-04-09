import sys
sys.stdin = open('5208.txt')

def DFS(n,charge,cnt):
    global sol
    if n==S:
        print(charge,cnt) #charge가 정류장수 이상이면서 cnt가 최소일때를 출력하면 될 것 같은데 # 중간에 방전되는 경우를 어떻게 알지
        # print(cnt)
        if charge >= N and sol > cnt:
            sol = cnt
        return

    DFS(n+1,charge+station[n],cnt+1)
    DFS(n+1,charge,cnt)


T = int(input())
for tc in range(1,T+1):
    data = list(map(int,input().split()))
    N = data[0] #N = 정류장개수
    S = data[0] - 1 #S = 충전소개수
    station = data[1:]
    sol = 123456789
    DFS(1,station[0],0)
    print(f"#{tc} {sol}")
