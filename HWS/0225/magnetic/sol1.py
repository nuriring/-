import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    result = 0
    for i in range(100):
        stack = 0
        for j in range(100):
            if data[j][i] == 1 and not stack:
                stack = 1
            elif data[j][i] == 2 and stack:
                result += 1
                stack = 0
    print(f'#{tc} {result}')


