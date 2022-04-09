import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N = int(input()) #정점의 개수
    arr = list(map(int,input().split()))
    tree = [0 for _ in range(N + 1)]
    # 시작 노드 번호가 1이므로 라스트도 1로 시작
    last = 1
    for i in range(len(arr)):  # 노드리스트로 반복 돌리기
        if not tree[last]:
            tree[last] = arr[i]  # 처음들어오는 9를 1번째 트리에 넣어야 한다
            # 그게 아니라면 완전 이지트리 모양을 맞추기 위해서 last가 1씩 증가
        else:
            last += 1
            child = last  # child와 parent 값을 비교해서 정렬해줘야 하니까
            parent = child // 2
            tree[child] = arr[i]
            # print(tree, parent, child)  # 정렬되지 않은 상태로 순차적으로 들어가고 있음
            # 부모가 가진 값이 자식이 가진 값보다 큰 동안
            while tree[parent] > tree[child]:  # 반복문으로 정렬시켜주자
                # 부모와 자식의 값을 서로 바꾼다.
                tree[parent], tree[child] = tree[child], tree[parent]
                # 자식 위치를 부모로 변경
                child = parent
                # 부모 위의 조상노드 찾아가기 그렇게 다시 정렬 #제일 적은 값을 루트로 끌어 올리는 과정, 최소힙 모양을 위해 꼭 필요함
                parent = parent // 2
                # 그러나 제일 위에 루트에만 최소힙이 오는 거지
                # 그 아래가  완전 정렬되는 것은 아님
    # print(tree)
    ssum = 0
    #마지막 노드의 조상노드 찾아가기
    while N//2: #부모노드가 존재하는 동안 반복
        ssum += tree[N//2]
        N = N//2 #부모노드를 다시 자기자신으로 할당
    print(f'#{tc} {ssum}')