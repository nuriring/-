import sys
sys.stdin = open('4874.txt')

T = int(input())
for tc in range(1,T+1):
    data = list(input().split())
    stack = []
    top = -1
    operator = ['+','*','/','-']
    # print(data)

    result = 0
    for i in data:
        if i in operator and len(stack)>=2: #연산자가 나왔는데 stack에 두개이상의 숫자가 있으면 연산가능
            if i == '+':
                sol = stack.pop(-2)+stack.pop(-1) # 먼저 꺼낸게 뒤로
                stack.append(sol)
            if i == '/':
                sol = stack.pop(-2)//stack.pop(-1) # 먼저 꺼낸게 뒤로
                stack.append(sol)
            if i == '-':
                sol = stack.pop(-2)-stack.pop(-1) # 먼저 꺼낸게 뒤로
                stack.append(sol)
            if i == '*':
                sol = stack.pop(-2)*stack.pop(-1) # 먼저 꺼낸게 뒤로
                stack.append(sol)
            #연산자가 나왔는데 스택의 길이가 2미만이면 연산 불가

        elif i not in operator and i!='.':
             stack.append(int(i))
        elif i in operator and len(stack) < 2:
            result = 'error'
            break
        elif i == '.' and len(stack) > 2:
            result = 'error'
            break
        result = stack[-1]



    print(f'#{tc} {result}')
