import sys
sys.stdin = open('4866.txt')

class Stack:
    def __init__(self, arr): #스택 객체 생성
        self.arr = arr
        self.top = -1

    def push(self, n): # 스택 요소 추가 push(.append())
        self.top += 1
        self.arr[self.top] = n

    def pop(self): # 스택 요소 삭제 pop()
        self.top -= 1
        return self.arr[self.top+1]

    def is_empty(self):  # 스택이 비었는지 확인(비었으면 True 리턴)
        if self.top == -1:
            return True
        else:
            return False

    def peek(self): # 스택 맨 앞 요소 리턴
        return self.arr[self.top]

T = int(input())
for tc in range(1, T+1):
    data = input()
    stack = Stack([0] * len(data)) #stack 사이즈 설정
    result = 0
    for i in range(len(data)):
        if stack.top == -1 and data[i] == '(': #스택이 비어있을때 괄호를 넣어줘야 내 방식으로 검사가능
            stack.push('(')
        elif stack.top == -1 and data[i] == '{':
            stack.push('{')
        elif data[i] == '(':#스택이 비어있지 않을때 괄호넣기 닫는 괄호가 안 나오는 경우 쌓아나갈수 있음
            stack.push('(')
        elif data[i] == '{':
            stack.push('{')
        elif data[i] == '}': #닫는괄호나오면
            if stack.peek() == '{': #괄호짝지가 일치하면 팝
                stack.pop()
            elif stack.is_empty() == True:
                break #스택이 비어있는데 닫는게 나오면 이미 잘못된 괄호니까
            else:
                break #괄호짝지가 일치하지 않아도 불일치로 break
        elif data[i] == ')':
            if stack.peek() == '(':
                stack.pop()
            elif stack.is_empty() == True:
                break
            else:
                break
    else:
        if stack.is_empty(): #짝지가 잘 맞아서 스택이 잘 비워진다면
            result = 1

    print(f'#{tc} {result}')