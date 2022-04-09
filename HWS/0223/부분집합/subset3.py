#부분집합의 합_ 이전까지 고려된 합에서 목표값 까지 도달하는 경우

def f(i, N,s, t):    # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, s는 이전까지 고려된 원소의 합, t는 목표값

    if s==t: #목표값을 찾으면 #i-1 원소까지의 합이 찾는 값인 경우
        for j in range(N): # 부분집합 원소의 갯수만큼 반복
            if bit[j]: #bit[j] 값이 1이라면
                print(a[j], end = ' ')
        print()
    elif i==N: #더 이상 고려할 원소가 없는 경우
        return


    else:
        bit[i] = 1 #bit 조사 처럼 i가 부분집합 원소의 갯수와 같아질때까지 재귀를 돌리면 된다
        f(i+1, N, s+a[i],t) #기존 더한값에 i원소를 포함해서 더해주기
        bit[i] = 0 #bit[i]=0이면 미포함
        f(i+1, N, s,t)
    return


N = 10
a = [x for x in range(1, N+1)] #

bit = [0]*N
t=27
f(0, N, 3, t)