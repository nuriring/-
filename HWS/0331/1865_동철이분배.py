import sys

sys.stdin = open('1865.txt')


def DFS(i, sol):
    global maxV

    if sol <= maxV:  # 가지치기 #확률은 1보다 작기때문에 곱해줄수록 더 작아지므로 가지치기를 해주면 더 작아지는 경우 굳이 더 곱해주지 않아도 된다.
        return

    if i == N:  # 이미가지치기에서 maxV보다 큰 결과만 살려뒀으니까
        maxV = sol  # 여기서는 따로 비교 없이 maxV값을 할당해주면됨
        return

    for j in range(N):  # 사용하지 않은 열들을 찾아서 순열로 만들어줌
        if visited[j] == 0:  # 아직 사용하지 않은 열이라면

            visited[j] = 1  # 방문표시
            DFS(i + 1, sol * Arr[i][j])  # 행 이동
            visited[j] = 0  # 원상복귀


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [0] * N
    Arr = [list(map(lambda x: x / 100, map(int, input().split()))) for _ in range(N)]  # 100나눠진 채로 입력받는 법
    # Arr = [list(map(int,input().split())) for _ in range(N)] 이렇게 해주면 DFS(i+1,sol*Arr[i][j]*0.01)

    maxV = 0
    DFS(0, 1)

    print(f'#{tc} {maxV * 100:6f}')
