# di=[-1,-1,1,1]
# dj=[-1,1,1,-1]
# def promising(si,sj):
#     flag = False
#     for idx in range(1,N+1):
#         if arr[si][idx] == 1: #퀸이 하나라도 놓여있으면
#             break
#         elif arr[idx][sj] == 1:
#             break
#
#     for k in range(4):
#         i,j = si,sj
#         while 1<=i<N and 1<=j<N:
#             ni = i+di[k]
#             nj = j+dj[k]
#             if arr[ni][nj] == 1:
#                 flag = False
#                 return flag
#             else:
#                 i,j = ni,nj
#
#     flag = True
#     return flag
#
# def checknode(si,sj):
#     global cnt
#     if promising(si,sj):
#         arr[si][sj] = 1
#         if si==N:
#             cnt+=1
#             return
#         else:
#
#             for j in range(1,N+1):
#                 checknode(si+1,j)
#
#
# N = 8
# cnt = 0
#
# visited = [[0]*(N+1) for _ in range(N+1)]
# arr = [[0]*(N+1) for _ in range(N+1)]
# checknode(1,1)
# print(cnt)

#  visited[n]의 값이 i라고 할 때 이는 n행 i열에 퀸이 있다는 의미이다.
#  즉 visited[1]의 값이 3라고 할 경우 이가 의미하는 것은 1행 3열의 위치에 퀸이 있는것이다.
# 같은 행에는 퀸이 겹칠일이 없음
# 대각선에 위치해있으면 행의 값차이와 열의값차이가 같다 ㅜㅜ
def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False
    return True


def checknode(n):
    global cnt
    if n == N:
        cnt += 1
        return
    else:
        for j in range(N):
            visited[n] = j
            if check(n):
                checknode(n + 1)


N = 2
cnt = 0

visited = [0] * N
checknode(0)
print(cnt)
