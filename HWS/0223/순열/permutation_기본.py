def f(i, N, r):
    if i==N: #순열완성
        print(p)
    else:
        for j in range(i,N):
            #i를 포함시켜야 자기자신 자리까지 포함되서 자리를 안바꾼 원본이 유지됨
            p[i], p[j] = p[j], p[i]
            f(i+1, N, r) #다음자리를 결정
            p[i], p[j] = p[j], p[i] #원상복귀

N = 3
p = [x for x in range(1, N+1)]
f(0, N, 2)

