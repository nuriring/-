#ABC 2
#DEF 3
#GHI 4
#JKL 5
#MNO 6
#PQRS 7
#TUV 8
#WXYZ 9

#숫자+1 만큼 시간이 걸림
alphabet = input()
time = 0
for alpha in alphabet:
    if alpha in 'ABC':
        time+=3
    elif alpha in 'DEF': 
        time+=4
    elif alpha in 'GHI': 
        time+=5
    elif alpha in 'JKL': 
        time+=6
    elif alpha in 'MNO': 
        time+=7
    elif alpha in 'PQRS': 
        time+=8
    elif alpha in 'TUV': 
        time+=9
    elif alpha in 'WXYZ': 
        time+=10
print(time)