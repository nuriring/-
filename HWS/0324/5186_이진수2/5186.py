import sys
sys.stdin = open('5186.txt')

T = int(input())
for tc in range(1,T+1):
    N = float(input())

    binary = ''  # 2진수
    cnt = 0
    while N != 0.0:
        N = N*2
        binary = binary + f'{int(N)}'
        cnt+=1
        N = N - int(N)
    # print(binary,cnt)
    if cnt>=13:
        print(f'#{tc} overflow')
    else:
        print(f'#{tc} {binary}')

# 또는
#     result = ''
#     while N != 0:
#         N *= 2
#         if N >= 1:
#             result += '1'
#             N -= 1
#         else:
#             result += '0'
#     print(f'#{tc}', end=' ')
#     if len(result) >= 13:
#         print('overflow')
#     else:
#         print(result)