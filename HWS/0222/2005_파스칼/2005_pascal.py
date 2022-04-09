import sys
sys.stdin = open('2005.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for i in range(N)]

    for i in range(N):
        for j in range(i+1): #행에 해당하는 열까지만
            if j-1<0: #2차원 배열의 가장 좌측은 모두 1
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j] #내부에 합 만들기 현재자리는 왼쪽위 숫자와 바로위 숫자의 합

    print(f'#{tc}')
    for i in arr:
        try:
            while True : i.remove(0) #0빼주는데 0이 없으면 인덱스 에러가 나므로 TRY EXCEPT로 에러처리해서 반복하게 해줌
        except ValueError:
            pass
        print(*i)
