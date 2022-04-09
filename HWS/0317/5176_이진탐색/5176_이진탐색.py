import sys
sys.stdin = open('input.txt')

T = int(input())
def binary_tree(i):
    global cnt
    if i <= N: #배열크기가 넘어가지 않도록한다 #완전이진트리를 만들기 때문에 비워있는 노드번호가 없다는거고 트리의 최대크기가 N을 벗어날수 없음
        binary_tree(2*i) # 왼쪽 노드는 현재 index의 2배이다 #좌측 #cnt가 커지기 전에 왼쪽에 집어넣고
        tree[i] = cnt # 값넣기  #내 위치에 집어넣고
        cnt += 1 #다음 숫자로 증가시키기
        binary_tree(2*i+1)#오른쪽 노드는 현재 index의 2배 + 1 #cnt가 커지고 난 뒤 오른쪽에 집어넣어줌

for tc in range(1,T+1):
    N = int(input()) #N은 정점의 갯수 1~N까지

    tree = [0 for _ in range(N+1)]
    cnt = 1
    binary_tree(1)
    print(f'#{tc} {tree} {tree[1]} {tree[N//2]}')
