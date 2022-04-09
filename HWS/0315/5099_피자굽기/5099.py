import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split()) #N은 화덕크기, M은 피자개수
    Cheese = list(map(int,input().split())) #M개의 피자에 뿌려진 치즈 양
    pizza = []
    for idx,C in enumerate(Cheese): #인덱스 번호를 피자번호로 저장
        pizza.append([idx+1,C])
    #print(pizza)
    '''
    [[1, 7], [2, 2], [3, 6], [4, 5], [5, 3]] [피자번호,치즈양]
    '''
    in_pizza = pizza[:N] #화덕의 크기만큼 피자넣기
    remain_pizza = pizza[N:] #남은 피자

    while len(in_pizza) > 1 : #화덕안에 피자가 한개 남으면 중단 #그 피자가 마지막 피자므로
        check = in_pizza.pop(0) #맨앞 피자 꺼내서 확인해보기
        check[1] = check[1]//2
        if check[1] == 0: #꺼냈을때 치즈가 다 녹아서 0 일 때
            if remain_pizza: #피자가 남아있으면
                in_pizza.append(remain_pizza.pop(0)) #화덕에 넣는다
        else: #꺼냈을때 치즈가 덜 녹았으면
            in_pizza.append(check) #다시 넣는다

    #한개 남았을 때 피자 번호 출력
    print(in_pizza)
    print(f'#{tc} {in_pizza[0][0]}')





