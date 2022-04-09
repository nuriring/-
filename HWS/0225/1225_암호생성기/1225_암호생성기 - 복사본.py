import sys
sys.stdin = open("input.txt")

for tc in range(1,11):
    tc = int(input())
    queue = list(map(int,input().split()))
    # print(data)
    #1~5까지 먼저 들어온것을 빼면서 뒤로 보내기 5까지가 한 cycle
    #맨 뒤가 0 이 되면 그때 암호가됨
    while queue[-1]!=0: #queue의 마지막이 0이 아닌동안 반복
        for i in range(1,6): #5번이 한 cycle
            if queue[0]-i > 0 : #첫번째값에서 1씩 늘려가면서 뺀값이 0보다 크다면
                queue.append(queue.pop(0)-i) #1씩커지면서 빼주고 뒤로 보내주는 걸 반복-> 이거를 마지막값이 0보다 작거나 같을때가지 반복
            else:
                queue.pop(0) #첫번째값에서 1씩 늘려가면서 뺀값이 0보다 작거나 같다면 첫번째 꺼 빼주고
                queue.append(0) #0으로 맨뒤에 넣어줌
                break #한번만 0이나오면 암호가 완성되므로 break

    print(f'#{tc}', *queue)