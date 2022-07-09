import sys
sys.stdin = open('4861.txt', 'r')

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    
    # 전체 2차원 배열
    words_arr = []
    # 가로 한줄씩
    for words in range(N):
        words = input()
        words_arr += [[x for x in words]]

        # 가로줄에서 찾기
        # 0 1 2 ...
        # for i in range(N-M+1):
        #     cnt = 0
        #     for j in range(M//2):
        #         if words[j+i] == words[i+M-1-j]:
        #             cnt += 1
        #             if cnt == M//2:
        #                 print('#{} {}'.format(tc, words[j+i-(M//2)+1:M+i]))

        for j in range(len(words_arr[0])):
            for i in range(len(words_arr)):
                # 세로줄에서 찾기
                for r in range(N-M+1):
                    jcnt = 0 
                    for l in range(M//2):
                        if words_arr[l+r][j] == words_arr[r+M-1-l][j]: # 인덱스가 벗어났다고 함 여기만 해결해주면 풀 수 있을 것 같음
                            jcnt += 1
                            if jcnt == M//2:
                                print('#{}'.format(tc), end=' ')
                                for k in range((l+r-(M//2)+1), M+r+1):
                                    print('{}'.format(words_arr[k][j]), end = '')
        print()

    print(words_arr)
