#부분집합의 합_재귀버전

def f(i, N, K):    # i 부분집합에 포함될지 결정할 원소의 인덱스, N 전체 원소개수, K 찾는 합

    if i==N:    # 한개의 부분집합 완성 0000000000~1111111111 인덱스를 1씩 늘리면서 N개와 같아졌다는것은 하나의 부분집합은 완성했다는 의미
        s = 0 #sum 구하기
        for j in range(N): # 부분집합 원소의 갯수만큼 반복
            if bit[j]: #bit[j] 값이 1이라면
                s += a[j]
    #         print(a[j], end = ' ')
    # print()
        if s==K: #찾는 합이면
            for j in range(N):
                if bit[j]:
                    print(a[j], end=' ')
            print()


    else:
        bit[i] = 1 #bit 조사 처럼 i가 부분집합 원소의 갯수와 같아질때까지 재귀를 돌리면 된다
        f(i+1, N, K) #인덱스i를 1씩 증가시키면서 조사 #bit[i]=1 이면 포함
        bit[i] = 0 #bit[i]=0이면 미포함
        f(i+1, N, K)
    return


N = 10
a = [x for x in range(1, N+1)] #

bit = [0]*N

f(0, N, 10)

