# DFS & 백트래킹 & 분할정복



### DFS

- 종류

  - 깊이 우선 탐색 DFS 

  - 너비 우선 탐색 BFS



- 알고리즘

  `EX` 4875_MAZE
  
  ```python
  def check(nx, ny): #이동 가능 여부 확인
      if 0 <= nx < N and 0 <= ny < N and arr[nx][ny]==1: #범위를 벗어나지 않고 벽이라면
          # 못간다
          return False
      return True #그 외에는 갈 수 있다
  
  dx = [0,1,0,-1] #우하좌상
  dy = [1,0,-1,0]
  
  
  def dfs(x,y):
      for k in range(4):
          nx = x+dx[k]
          ny = y+dy[k]
          #경계조건
          if 0 <= nx < N and 0 <= ny < N:
              if arr[nx][ny] == 3: #한번이라도 도착했다면#함수 끝내기
                  return 1 #return으로 도착햇다는 사실 메아리로 알리기
              else: #아직도착못했다면
                  if check(nx,ny): #이동가능하다면
                      arr[nx][ny] = 1 #방문 표시, 따로 배열을 안만들어주는 이유는 한번 갔던 길은 이미 유망성이 낮기 때문
                      is_arrive = dfs(nx,ny) #다음 위치로 이동 #재귀호출 사용
                      if is_arrive: #재귀호출 값이 도착했다는 1이라면
                          return 1
      return 0#dfs를 다 수행했는데 return1에 걸리지 못했다는 것은 막힌 미로라는 것을 의미
  
  T = int(input())
  for tc in range(1,T+1):
      N = int(input())
      arr = [list(map(int,input())) for _ in range(N)]
  
  
      for i in range(N):
          for j in range(N):
              if arr[i][j] == 2:
                  result = dfs(i,j)
                  #깊이 탐색 시작할 출발점
                  break
      print(f'#{tc} {result}')
  ```
  
  `EX` 4871_Graph
  
  ```python
  def dfs(v):
      visited[v] = 1 #방문했다면 True표시
      for w in range(1, V+1): #노드갯수만큼 반복 #오름차순으로 검색하는것과 같은 의미
          if data[v][w] == 1 and visited[w] == 0: #길이있고 방문하지 않았다면
              dfs(w) #w가 다시 v가 된다
  
  T = int(input())
  for tc in range(1,T+1):
      V,E = map(int,input().split()) #V는 노드의 개수 E는 간선의 개수 #노드번호는1번부터
      data = [[0]*(V+1) for _ in range(V+1)] #길을 기록할 이차원 배열
      for _ in range(E):
          s,e = map(int,input().split()) #s는 출발 노드 e 도착노드
          data[s][e] = 1 #길을 기록
      # pprint(visited)
      check_s,check_e = map(int,input().split()) #경로가 있으면 1 없으면 0
  
      visited = [0]*(V+1) #방문했는지를 기록할 1차원 배열 모두 False로 초기화
  
      dfs(check_s) #출발점에서 깊이탐색 시작작
  
      #다 조사한뒤 확인할 도착점의 visited 가 1 이라면 경로가 있다는 것을 의미
      print(f'#{tc} {visited[check_e]}')
  ```
  
  

### Backtracking

`EX` 부분집합 원소의 합이 10 인 원소를 출력하기 (끝판왕이니 simple한 버전 먼저 사용할수있게 공부한 후 습득)

```python
def process_solution(arr, k, result):
    if result != 10: #부분집합의 합이 10이 아니라면!
        return
    #10이라면 아래 작업이 수행된다
    for i in range(1, k+1):
        if arr[i]:
            print(data[i], end=' ')
    print()

def construct_candidator(arr, k, N, c):
    # 부분집합을 구할 것이기 때문에
    # 넣거나 안넣거나 2가지 경우의 수 밖에 없음
    c[0] = True
    c[1] = False
    return 2

# arr : 해당 원소를 사용했는지 안했는지, 원소를 직접 집어 넣을 list
# k : 현재 어디까지 조사중인지 확인할 (현재 몇개까지 만들어졌는지 나타내는 원소갯수)
# N : 내가 최대 조사해야 할 대상의 길이
# result
def backtracking(arr, k, N, result):
    global cnt
    # 유망성 조사를 할 리스트 #가지치기
    if result > 10:
        return

    c = [0] * MAXCANDIDATES

    # 현재 조사상황 == 최대 조사 상황 (재귀의 기저까지 왔다면)
    if k == N:
        # 내가 원하는 수식이 만들어 졌는지 확인할 함수 #답이면 원하는 작업을 한다
        process_solution(arr, k, result)
    else:
        k += 1
        ncandidates = construct_candidator(arr, k, N, c) #1과0을 사용해서 후보군 추천 방법을 사용하면되
        for i in range(ncandidates):
            # 내가 집어 넣어준 arr의 k번째의 값을 쓰거나 안쓰거나
            arr[k] = c[i]
            if arr[k]:
                backtracking(arr, k, N, result + data[k])
            else:
                backtracking(arr, k, N, result)
    cnt += 1

# 유망성 조사를 위한 변수
MAXCANDIDATES = 100
NMAX = 100

cnt = 0
data = list(range(11))
arr = [0] * NMAX
backtracking(arr, 0, 10, 0)
print(cnt)
```



`EX` 순열  (끝판왕이니 simple한 버전 먼저 사용할수있게 공부한 후 습득)

```python
def process_solution(a, k, sum):
    global cnt
    # if sum != 10:
    #     return
    for i in range(1, k + 1): #1에서k까지
        if a[i]: 
            print(data[i], end=" ")
    print()
    cnt += 1

def construct_candidates(a, k, input, c):
    in_perm = [False] * NMAX #사용하지않은 상태로 초기화

    for i in range(1, k): #1에서 k-1까지
        # 앞부분에서 사용된적이 있으면 True 로 체크
        in_perm[a[i]] = True
    ncandidates = 0
    for i in range(1, input + 1):
        # 사용된적이 없는 요소들을 기준으로 확인
        if in_perm[i] == False:
            c[ncandidates] = i
            ncandidates += 1
    print(c)
    return ncandidates

# a: 해당 원소를 사용 할 것(o) / 안할 것(x) 여부
# k: index
# input: #내가 최대 조사해야할 대상의 길이
def backtrack(a, k, input):
    global total_cnt

    c = [0] * MAXCANDIDATES
    
    if k == input:
        for i in range(1, k+1):
            print(a[i], end= ' ')
        print()
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k, input)

MAXCANDIDATES = 6
NMAX = 6 #input값 5까지 인덱스 에러나지 않고 가능
data = [range(10)]
a = [0] * NMAX
cnt = 0
total_cnt = 0
backtrack(a, 0, 5) #input이 3이면 1,2,3 세개로 만들 수 있는 순열이 출력된다

```



### Quick Sort



### 결론

완전탐색의 종류에 조합,순열,부분집합이 있다

조합, 순열, 부분집합을 자연스럽게 만들줄 알아야 한다

위의 것들을 이용해서 연산을 하기 때문 

이 연산을 간략화하는 과정에 백트래킹까지 곁들여진다.
