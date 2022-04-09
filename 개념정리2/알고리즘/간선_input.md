### 인접행렬 또는 인접리스트

```python
'''
input data
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

'''

V, E = map(int, input().split()) #노드의 범위 1~7까지, E는 간선의 갯수
data = list(map(int, input().split())) #간선 정보
adjGrid = [[0]*(V+1) for _ in range(V+1)]  #인덱스번호맞추기
adjList = [[] for _ in range(V+1)]
for i in range(E):
    n1, n2 = data[i*2], data[i*2+1]
    adjGrid[n1][n2] = 1     # n1과 n2는 인접
    adjGrod[n2][n1] = 1     # 방향 표시가 없는 경우 반대방향도 표시해줌
	'''
    adjGrid[data[0]][data[1]] = 1
    adjGrid[data[1]][data[0]] = 1

    adjGrid[data[2]][data[3]] = 1
    adjGrid[data[3]][data[2]] = 1
	'''
    adjList[n1].append(n2) # n1과 n2는 인접
    adjList[n2].append(n1) # 방향 표시가 없는 경우

for i in range(len(data)//2): #방향 표시가 있는 경우
     adjList[n1].append(n2) 
	# 단방향 인접리스트 출력 예시	
	# [[], [2, 3], [4, 5], [7], [6], [6], [7], []] #길1은 2,3과 인접 / 길2는 4,5와 인접..
 
```



