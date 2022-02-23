#직사각형 경계선까지의 최단거리
#(x,y)는 직사각형 내부에 위치
numlist = list(map(int,input().split())) #input값을 리스트로 받는다 [x,y,w,h]
x = numlist[0]
y = numlist[1]
w = numlist[2]
h = numlist[3]
dis_list = [x, y, h-y, w-x] #직사각형 경계선까지 거리의 경우의 수를 dis_list에 담는다
for dis in dis_list: #dis_list 내에서 최솟값 구하기
    if dis_list[0]>=dis:
        dis_list[0]=dis
print(dis_list[0])