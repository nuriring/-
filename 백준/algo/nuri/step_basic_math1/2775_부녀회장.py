
k = 5 #k층
n = 5 #n호 에는 몇명이 살고 있을까?
#k층 n호에는 k-1층의 1~n호 까지의 사람수 합이 살아야 한다
#0층부터 시작해서 k-1층의 1~n호까지 사람수를 누적해 나가야 한다

#floor = [0]*n #1~n호까지 사람수를 넣어줄 배열을 만든다
#0층의 사람수 
# floor0 = list(range(1,n+1))
# floor1 = 0
# for i in range(n-1):
#     floor0[i+1]+=floor0[i]
# floor1 = floor0
# for i in range(n-1):
#     floor1[i+1]+=floor1[i]
# print(floor1)

#k번 반복
person = list(range(1,n+1)) #0층에서 n호까지 사람 수 
floor = 0 #0층에서 k층까지 반복
while floor!=k: #층수가 k가 아닌동안 한층씩 높여가면서 반복
    for i in range(n-1): #1에서 n호까지
        person[i+1]+=person[i] #n-1호까지의 합이 n호에 누적됨


    floor += 1 #1층씩 증가 
print(person[-1])