import sys
sys.stdin = open('1223.txt.txt')

for tc in range(1,11):
    N = int(input())
    data=input()
    stack = []
    lst = ""
    #우선순위가 높으면 push
    #우선순위가 낮거나 같은게 나올때까지 pop #pop한 것은 연산리스트에 저장
    #여는괄호는 가장 우선순위가 높으므로 push
    #닫는괄호가 나오면 여는괄호가 나올때가지 pop #pop한 것은 연산리스트에 저장
    #숫자는 연산리스트에 저장
    for i in data:
        if i.isdecimal():
            lst+=i
        # print(lst)
        elif i=='*':
            while stack and stack[-1]=='*': #곱하기 나누기 우선순위가 서로 같을때
                lst+=stack.pop()
            stack.append(i)
        elif i=='+':
            while stack and (stack[-1]=='*' or stack[-1]=='+'): # 이거는 우선순위가 가장낮은 '('괄호가 아닐때랑 같음
                lst+=stack.pop()
            stack.append(i)

    else:#반복다한 후에도 스택에 뭐가 차있으면 비워내줌
        while stack:
            lst+=stack.pop()
    print(lst)
    operator = ['+','-','*','/']
    for i in lst:
        if i in operator and len(stack) >= 2:  # 연산자가 나왔는데 stack에 두개이상의 숫자가 있으면 연산가능
            if i == '+':
                sol = stack.pop(-2) + stack.pop(-1)  # 먼저 꺼낸게 뒤로
                stack.append(sol)
            if i == '*':
                sol = stack.pop(-2) * stack.pop(-1)  # 먼저 꺼낸게 뒤로
                stack.append(sol)

        elif i not in operator:
            stack.append(int(i))
    result = stack[-1]

    print(f'#{tc} {result}')
