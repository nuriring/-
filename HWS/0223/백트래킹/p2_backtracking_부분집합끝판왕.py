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
    if result > 10: #합이 10보다 커지면 return
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