import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    data = input()

    stack = []
    for char in data:
        if not stack:
            stack.append(char)
        elif char != stack[-1]:
            stack.append(char)
        else:
            stack.pop()
    print(f'#{tc} {len(stack)}')