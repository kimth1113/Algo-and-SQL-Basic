import sys
sys.stdin = open('4837.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, K = map(int, input().split())

    arr = [0] * 12
    for i in range(1, 13):
        arr[i-1] = i
    
    result = 0 # 부분집합의 갯수
    for i in range(1<<12):
        cnt = 0 # 원소의 갯수
        total = 0 # 원소들의 합
        for j in range(12):
            if i & (1<<j):
                cnt += 1 # 갯수 +1
                total += arr[j] # 합 +arr[j]
        if cnt == N and total == K:
            result += 1 # 부분집합
        
                
    print('#{} {}'.format(tc, result))
        
