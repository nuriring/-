def quickSort(a, begin, end) :
    if begin < end :
        p = partition(a, begin, end)
        quickSort(a, begin, p-1) #분할 후 왼쪽 부분에서 정렬 수행
        quickSort(a, p+1, end) #분할 후 오른쪽 부분에서 정렬 수행

def partition (a, begin, end) :
    pivot = (begin + end) // 2 #첫번째 피봇 중간자리
    L = begin #인덱스 왼쪽 끝 0
    R = end # 인덱스 오른쪽 끝 -1
    while L < R : #피봇인L이 R과 자리를 바꿔서 L이 더 커져버릴때까지, L과 R이 같아져서 피봇과 자리교환을 통해 피봇의 자리가 확정될때까지 반복수행
        while(L<R and a[L]< a[pivot]):
            L += 1 #좌측에서 피봇보다 큰 원소를 찾을때까지 우측으로 이동
        while(L<R and a[R]>=a[pivot]):
            R -= 1 #우측에서 피봇보다 작은원소를 찾을때까지 좌측으로 이동
        if L < R :#찾아서 while반복문이 끝났는데 l과 r이 이미 엇갈렸다면 이 구문에 들어오지 않음
            if L==pivot : ##이전에 피봇과 R의 자리를 바꾸고 난후 다시 되돌려줘야 한다
                pivot = R
            a[L], a[R] = a[R], a[L] #여전히 R이 크다면 서로 맞바꿔주는 작업을 진행한다
    a[pivot], a[R] = a[R], a[pivot] #이미 엇갈렸다면 피봇의 위치를 그대로 결정해주면 됨
    return R #L과R이 만나므로 L로 해줘도 결과는 같게나옴

a = [11,45, 23, 81, 28, 34]
quickSort(a, 0, len(a)-1)
print(a)