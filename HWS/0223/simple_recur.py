def f(i, N):
    if i==N: #재귀함수의 종료조건
        return
    else:
        B[i] = A[i]
        f(i+1, N) #인덱스가 리스트의 길이와 같아질때까지

A = [10, 20, 30]
B = [0]*3
f(0, 3)
print(B) #동일한 [10,20,30]이 출력된다