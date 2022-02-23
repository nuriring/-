import sys
sys.stdin = open('2605.txt')
N = int(input())
lst = list(map(int,input().split()))
line = []

i=1
while len(line)<N:
    line.append(i)
    j = lst[i-1]
    line[i-1-j],line[i-1] = line[i-1], line[i-1-j]
    i+=1
print(line)

