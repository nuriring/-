import sys
sys.stdin = open('5247.txt')
from collections import deque
# 연산의 중간 결과도 항상 백만 이하의 자연수여야 한다. 결과가 음수면 append를 안해줘도 된다는 의미겠지
# 원하는 값에 도달하면 그만 돌려도 된다는 거지
def bfs(s, cnt):
    global result
    q = deque()
    q.append((s, cnt))
    visited[s] = 1
    while q:
        num, count = q.popleft()
        # cnt += 1 이렇게 하면 다 따로따로 cnt를 올려주니깐 cnt 값도 큐에다가 넘겨줘서 세줘야 bfs 돌때마다 한번씩 증가시킬수 있음
        if num == M:
            result = count
            return

        for op in operation:
            if op[0] == '+':
                if 0 < num + op[1] <= 1000000 and visited[num + op[1]] == 0:
                    q.append((num + op[1], count + 1))
                    visited[num + op[1]] = 1
            elif op[0] == '-' and op[1] == 1 and visited[num - op[1]] == 0:
                if 0 < num - op[1] <= 1000000:
                    q.append((num - op[1], count + 1))
                    visited[num - op[1]] = 1
            elif op[0] == '*':
                if 0 < num * op[1] <= 1000000 and visited[num * op[1]] == 0:
                    q.append((num * op[1], count + 1))
                    visited[num * op[1]] = 1
            elif op[0] == '-' and op[1] == 10:
                if 0 < num - op[1] <= 1000000 and visited[num - op[1]] == 0:
                    q.append((num - op[1], count + 1))
                    visited[num - op[1]] = 1

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    operation = [('+', 1), ('-', 1), ('*', 2), ('-', 10)]
    visited = [0] * 1000001
    result = 0
    bfs(N, 0)
    print(f"#{tc} {result}")
