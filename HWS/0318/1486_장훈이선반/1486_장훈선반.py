import sys
sys.stdin  = open('input.txt')

def DFS(n,ssum): #n은 인덱스
    global ans
    if ssum >= B+ans: #가지치기, 더 가봤자 의미가 없으므로 #이미 정답을 넘어간경우 #최소차이를 찾아주는 것이기 때문에 ssum이 선반에 최소차이인정답을 더한 값을 이미 넘어간 경우 더 볼 필요 없음
        return

    if n==N:
        if ssum >= B and ans>ssum-B:#키로 만든탑이 선반이상이 되면 -> 키로 만든탑과 선반 높이의 차가 작을수록 갱신해서 최소차이를 찾아준다
            ans = ssum-B
        return
    DFS(n+1,ssum+lst[n]) #포함하는 경우
    DFS(n+1,ssum) #포함하지 않는 경우 모두 탐색해준다

T =int(input())
for tc in range(1,T+1):
    N, B =map(int,input().split())
    lst = list(map(int,input().split()))
    ans = 12345678
    DFS(0,0)
