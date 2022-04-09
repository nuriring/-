import sys
sys.stdin = open('input.txt')

#좌중우 #중위순회 연산
def calc(operation,a,b):
    if operation == '*':
        return a*b
    elif operation == '/':
        return a/b
    elif operation == '+':
        return a + b
    elif operation == '-':
        return a - b

def in_order(node):
    if node:
        if tree[node][0] in ['*','-','/','+']:
            #왼쪽 자식
            left_num = in_order(tree[node][2])
            #중앙
            operation = tree[node][0]
            #오른쪽 자식
            right_num = in_order(tree[node][3])
            return calc(operation,left_num,right_num)
        else: #숫자면
            return tree[node][0]

for tc in range(1,11):
    N = int(input()) #정점의 총수
    # tree = [[0,0,0,0] for _ in range(N+1)]
    tree = [['',0,0,0] for _ in range(N+1)]
    for _ in range(N): #N줄에 걸쳐 정점 정보
        edge = list(map(str,input().split()))
        if len(edge) == 4:
            node, operation, ch1, ch2 = int(edge[0]), edge[1], int(edge[2]), int(edge[3])
            tree[node][0] = operation
            tree[node][2] = ch1
            tree[node][3] = ch2
        else:
            node, value = int(edge[0]), int(edge[1])
            tree[node][0] = value
    print(tree)

    result = in_order(1)
    print(f'#{tc} {int(result)}')