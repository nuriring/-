import sys
sys.stdin = open('1223.txt.txt')



for tc in range(1, 11):
    N = int(input())
    word = input()
    stack = []
    result = ''

    for char in word:
        if char in '*/+-()':
            if not stack:
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char in '*/':
                while stack and stack[-1] in '*/':
                    result += stack.pop()
                stack.append(char)
            elif char in '+-':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    result += stack.pop()
                stack.pop()
        else:
            result += char

    while stack:
        result += stack.pop()

    for char in result:
        if char not in '*/+-':
            stack.append(int(char))
        else:
            if len(stack) >= 2:
                x = stack.pop() #처음 뽑은거
                y = stack.pop() #두번째로 뽑은거
                if char == '+':
                    stack.append(y + x)
                elif char == '-':
                    stack.append(y - x)
                elif char == '*':
                    stack.append(y * x)
                elif char == '/':
                    stack.append(y / x)
    print(f'#{tc} {stack[-1]}')