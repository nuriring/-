import sys
sys.stdin = open('input.txt')
#N이 16이하 백트래킹으로 가능한 경우를 다 구해보자
#식재료가 A에들어가거나 B에 들어가거나 두가지 경우 밖에 없음
#종료조건이 되면 두개의 음식 맛 차이를 구해야함

# A음식에 들어가는 N/2개의 식재료 리스트를 alst 에 담아서 넘기고
# B음식에 들어가는 N/2개의 식재료 리스트를 blst에 담아서 넘겨주자
# 두개가 N/2로 반띵이 된다는거는 두 리스트 길이가 똑같다는 것을 의미

def DFS(n, alst, blst):
    global ans
    if n==N: # 종료조건 식재료를 다 조사했고
        if len(alst)==len(blst): # ==N//2 랑 같은상황
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)): #두개의 길이는 같으니까 상관없음
                    asum += S[alst[i]][alst[j]] #두개씩 식재료 나눠지면 A에 들어가는 음식 시너지 합해줌
                    # #이렇게 하면 두개의 식재료가 같을때도 들어가게 되지만 i와j가 모두 0일때
                    #현재는 식재료가 같을때 시너지가 0이므로 같을때를 제외해줄 필요는 없음
                    #얘를들어 식재료가 4개면 0,0 0,1 1,0 1,1 이렇게 i,j에 들어가는데
                    #a리스트에 식재료 조합이 0,1 0,2 0,3 0,4 1,2 2,3 3,4 #이런식으로 모든 조합이 다 들어갈 수 있음
                    bsum += S[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    DFS(n+1,alst+[n],blst) # 식재료 바꿔가면서 a음식에 넣고 , b음식에 안 넣고
    DFS(n+1,alst,blst+[n])



T = int(input())
for tc in range(1,T+1):
    N = int(input())
    S = [list(map(int,input().split())) for _ in range(N)]
    ans = 12345678
    DFS(0,[],[]) #0은 식재료 인덱스번호, 아직 아무런 식재료도 들어가지 않았으니까 초기에는 빈리스트
    print(f'#{tc} {ans}')
