def process_solution(a, k, sum):
    global cnt
    # if sum != 10:
    #     return
    for i in range(1, k + 1): #1에서k까지
        if a[i]: 
            print(data[i], end=" ")
    print()
    cnt += 1

def construct_candidates(a, k, input, c): # 내가 만든 순열에 아직 들어가있지 않은 숫자를 뒤짐
    in_perm = [False] * NMAX #사용하지않은 상태로 초기화 #visited랑 비슷함

    for i in range(1, k): #1에서 k-1까지 , k번째 숫자를 선택하기위해 k-1까지 뒤지는거임
        # 앞부분에서 사용된적이 있으면 True 로 체크
        in_perm[a[i]] = True
    ncandidates = 0
    for i in range(1, input + 1): #우리에게 주어진 숫자, 사용할 수 있는 숫자들
        # 사용된적이 없는 요소들을 기준으로 확인
        if in_perm[i] == False:
            c[ncandidates] = i #c에 사용되지 않은 숫자를 집어 넣어줌
            ncandidates += 1 #ncands 갯수만큼 c에 들어가게됨
    print(c)
    return ncandidates

# a: 해당 원소를 사용 할 것(o) / 안할 것(x) 여부
# k: index
# input: #내가 최대 조사해야할 대상의 길이
def backtrack(a, k, input):
    global total_cnt

    c = [0] * MAXCANDIDATES
    
    if k == input: ##여기서 process solution을 해준거임
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
