arr = list(range(1, 11))

N = len(arr)

def powerset(arr, idx, total):

    # 언제까지 재귀로 순회할 것이냐
    # 내가 가지고 있는 모든 원소를 조사 했을때
    if idx == N:
        print(total) 
        return
    # arr, 다음 조사 대상, 현재 조사대상을 total에 넣거나
    powerset(arr, idx + 1, total + [arr[idx]])

    # 안 넣거나
    powerset(arr, idx + 1, total)


powerset(arr, 0, [])
