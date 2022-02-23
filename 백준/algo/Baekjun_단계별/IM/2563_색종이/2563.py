import sys
sys.stdin = open('2563.txt')

T = int(input())
area = 0
arr = [[0]*100 for _ in range(100)]
for _ in range(1,T+1):
    j,i = map(int,input().split())
    #print(arr)
    for i in range(i,i+10):
        for j in range(j,j+10):
            #print(i,j)
            if arr[i][j] == 0:
                arr[i][j] += 1
                area += 1
print(area)