import sys
sys.stdin = open('2382.txt')
from pprint import pprint

T = int(input())
di,dj = (0,-1,1,0,0),(0,0,0,-1,1) #인덱스 번호 맞춰주기 1:상, 2:하, 3:좌, 4:우
opp = [0,2,1,4,3] #방향 반대로바꿀때 룩업테이블
for tc in range(1,2):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(K)] #[[i,j,cnt,dir]]
    for _ in range(M): #격리시간동안
        # [1] 각각의 미생물 이동 후 경계 처리
        for i in range(len(arr)):
            arr[i][0] = arr[i][0] + di[arr[i][3]] #각각의 위치에서 세로로 이동
            arr[i][1] = arr[i][1] + dj[arr[i][3]] #각각의 위치에서 가로로 이동
            if arr[i][0] == 0 or arr[i][0]==N-1 or arr[i][1] == 0 or arr[i][1]== N-1: #가로세로 경계조건 약품 칠해놓은곳에 도달하면
                arr[i][2]//=2 #세균수 반으로 줄어들고
                arr[i][3] = opp[arr[i][3]] #방향은 반대방향

        #[2] 정렬 (좌표, 개수) 내림차순 #좌표 같으면 인접해 있고, 숫자가 더 큰 미생물에 적은 미생물은 합쳐지고 없애버리기 위해 sort로 내림차순으로 정렬
        arr.sort(key=lambda x :(x[0],x[1],x[2]), reverse=True) #x[0] 이 같으면 x[1]을 기준으로 , x[1]이 같으면 x[2]를 기준으로 정렬한다는 의미
        ## 좌표가 같으면서 미생물수가 큰게 위로오도록 내림차순으로 정렬가능한거임

        # [3] 같은 좌표인 경우, 큰 미생물로 합치기 # 그 소팅된 arr를 활용해서 미생물 큰놈에 합쳐주기기
        i = 1 #제일위에는 가장 미생물수가 많으니까
        while i<len(arr):
            if arr[i-1][0] == arr[i][0] and arr[i-1][1] == arr[i][1] : #위의 미생물과 좌표를 비교했을 때 좌표가 같다면
                arr[i-1][2] += arr[i][2] #위에 가 나보다 크니까 위에 나를 합쳐줌
                arr.pop(i) #그리고 나를 제거
            else:
                i+=1

    ans = 0
    for i in range(len(arr)): #미생물 수 세어주기
        ans += arr[i][2]

    print(f'#{tc} {ans}')