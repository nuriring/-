import sys
sys.stdin = open('2669.txt')

arr = [[0]*100 for _ in range(100)]
area = 0
for i in range(4):
    i1,j1,i2,j2 = map(int,input().split())
    for i in range(i1,i2):
        for j in range(j1,j2):
            if arr[i][j] == 0:
                arr[i][j] += 1
                area +=1
print(area)
