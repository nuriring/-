n=0
generated_list=set() #중복을 막기 위해서 set함수를 사용
while n<10000:
    num = n #n값을 나중에 사용해야 하기 때문에 num에 따로 할당
    digit_sum = 0
    while num>0: 
        remainder = num%10     
        digit_sum+=remainder #자릿수의 합
        num=num//10
    generated_list.add(n+digit_sum) # 위치 주의 while문 안에서 추가를 하면 생성자가 없는 수도 만들어 질수 있다
    n+=1

natural_num = set(range(1,10001)) #일반 자연수에서
self_num = natural_num - generated_list #생성자가 있는 수의 차집합을 구해주면 셀프 넘버다
for self_num in sorted(self_num): #리스트 내부 숫자 출력
    print(self_num)


#문자열로 풀어보자
#39 = 33 + 3 + 3
#숫자 n이 입력되면 string으로 바꿔준다


# generated_list=set() #중복 생성자가 있는 숫자를 없애주기 위해서
# for n in range(1,10001):
#     for num in str(n):
#         n+=int(num) #각 자릿수의 합
#     generated_list.add(n)

