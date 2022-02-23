# String

## 패턴 매칭에 사용되는 알고리즘

- 고지식한 패턴 검색(Brute-Force)
- 카프 라빈
- KMP
- 보이어-무어



### Brute-Force

```python
p = 'is' #찾을 패턴
t = 'This is a book'
M = len(p) #찾을 패턴의 길이
N = len(t) #전체 텍스트의 길이

def BruteForce(p,t):
    i = 0 #t의 인덱스
    j = 0 #p의 인덱스
    while j<M and i<N:
        if t[i] != p[j]:
            i = i-j
            j = -1
        i = i+1
        j = j+1
    	if j==M:
            return True #검색 성공
        	#j = 0 #만일 테스트 케이스가 여러개라면 다음 대조 대상 초기화 
    else:
    	return -1 #검색 실패
        
        
```



### KMP

```python
def KMP(pattern, target):
	p_idx = 0
    p_len = len(pattern)
    t_idx = 0
    t_len = len(target)
    cnt = 0
    while p_idx<p_len and t_idx<t_len:
        a = pattern[p_idx]
        b = target[t_idx]
        #매칭되지 않았을 때,
        if a != b:
            #패턴의 첫글자였다면
            if p_idx == 0:
                #target의 조사대상만 1이동
                t_idx += 1
            else: #아니면
                p_idx = 0 #target은 그대로 p만 처음부터
        #두 글자가 같다면
        else: 
            #다음 조사 위치로
            t_idx += 1
            p_idx += 1
        if p_idx == p_len:
            return True #검색 성공
   	else:
        return -1 #검색 실패
        
```



### 보이어-무어

```python
def search(pattern, char):
    #어디까지 동일한 값을 가지고 있는지 확인
    for i in range(len(pattern)-2,-1,-1):
        #동일한 값이 있다면
        if pattern[i] == char:
            #확인한 위치까지 이동
            return len(pattern)-i-1
        #없다면 패턴 길이만큼 이동
        return len(pattern)

def Boyer_moore(pattern, target):
    p_len = len(pattern)
    t_len = len(target)
    t_idx = 0
    #조사 대상은 idx가 전체 길이 - 패턴 길이를 넘기 전까지
    while t_idx <= t_len-p_len:
        p_idx = p_len-1
        #보이어 무어는 뒤에서부터 조사하므로
        #패턴의 조사대상이 0 보다 큰 동안
        # 즉, 뒤에서부터 처음까지 조사활동 반복
        while p_idx >= 0:
            a = pattern[p_idx]
            b = target[t_idx + p_idx]
            #만약 두 대상이 현재 같지 않다면
            if a != b:
                #다음 조사 위치로 이동하기 위한 값 색출
                next = search(pattern, target[t_idx+p_len-1])
                break
            #아니라면 조사대상 index-=1
            p_idx -= 1
        #끝까지 조사했다면
        if p_idx == -1:
            #매칭
            return 1
        #아니라면 다음 조사 위치로 이동
        else:
            t_idx += next
    return 0
```





