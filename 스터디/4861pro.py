import sys
sys.stdin = open("4861.txt", "r")

def chkP(chkstr):
    #print(chkstr)
    l = len(chkstr)
    for i in range(l//2-1):
        if chkstr[i] != chkstr[l-1-i]:
            return False
    return True

def allChk():
    for n in range(N):
        for i in range(N - M + 1):
            # 가로시작점
            if chkP(BRD[n][i:i + M]):
                return BRD[n][i:i + M]

            # 세로시작점
            tempS = ''
            for k in range(i, i + M):
                tempS = tempS + BRD[k][n]
            if chkP(tempS):
                return tempS

    return ''

TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    BRD = [input() for _ in range(N)]

    print('#{} {}'.format(tc, allChk()))

    #print(BRD[0][1], BRD[1][1])
    #전체 가로줄


