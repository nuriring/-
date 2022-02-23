# N킬로 그램의 설탕을 배달
# 3킬로 봉지와 5 킬로 봉지가 있음
# 최대한 적은 봉지를 들고 가려고 함
# N이 input으로 주어진다
N = int(input())
# N 킬로그램으로 만들수 없다면 -1을 출력

##5와 3의 최소합으로 N을 만드는데 최대한 적은 봉지를 가지고 갈려면 5kg을 더 많이 활용
#따라서 sugar에서 3을 떼어가다가 5의 배수가 되면 종료
sugar = N
bag = 0
while sugar>=0: #0보다 크다고 하면 3의 배수인 경우 else 문으로 빠져버리므로 주의
    if sugar%5==0:
        bag +=sugar//5
        print(bag) #print (bag) 위치 중요
        break #5로 나눠줄수 있으면 while 문 break
    sugar-=3 #sugar에서 3을 빼주다가 5로 나눌수 있을 때 다시 if문에 걸리게 된다
    bag+=1

else: #3을 계속 빼줘도 5로 나눠줄수도 없고 sugar의 수가 음수가 되는 등 3과5의 합으로 만들수 없을 때 while-else문에 걸림 
    print(-1)
