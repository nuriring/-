import sys
sys.stdin = open('5201.txt')
T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split()) #N은 컨테이너 수 , #M은 트럭수
    weight = list(map(int,input().split()))
    limit = list(map(int,input().split()))

    s_weight = sorted(weight,reverse=True)
    # print(s_weight)
    s_limit = sorted(limit,reverse=True)
    # print(s_limit)
    sol = []
    # while s_weight and s_limit: #트력도 있고 화물도 있어야 실어나를 수 있음 둘중에 하나라도 없으면 그때부터 동작그만되니깐
    for i in range(len(s_weight)): #무거운 것 부터 실어주기
        if s_weight[i]<=s_limit[0]:
            s_limit.pop(0)
            sol.append(s_weight[i])
            if not s_limit:
                break
        else:
            continue
    print(f'#{tc} {sum(sol)}')


