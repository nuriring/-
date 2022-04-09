def permutation(i, N, r):
    if i == N:
        print('='*15, P[0:r], '='*15)
        print()
    else:
        for j in range(i, N):
        #각 depth에 대해 남아 있는 것들 중에 모두 뽑아보고,
        #해당 경우에 대해 재귀적으로 perm함수를 돌리고,
        #원상복구 하여 다시 경우의 수를 찾는다
            P[i], P[j] = P[j], P[i]
            print(P, 'front', i, j)
            permutation(i+1, N, r)
            P[i], P[j] = P[j], P[i]
            print(P, 'back', i, j)


P = [1, 1, 3, 4]
permutation(0, len(P), 2)

