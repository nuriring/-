import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())

    n = n // 10

    '''
    1 = 1
    2 = 3
    3 = 5
    4 = 11
    5 = 21
    6 = 42
    '''
    memo = [1, 3]
    for i in range(2, n):
        memo.append(memo[i-1] + memo[i-2]*2)
    print(f'#{tc} {memo[n-1]}')

