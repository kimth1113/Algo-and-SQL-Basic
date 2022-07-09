import sys
sys.stdin = open('1216.txt', 'r')

def BruteForce(word, words):
    i = 0
    j = 0
    while j < M and i < N:
        if words[i] != word[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == M: return 1
    else: return 0

TC = 10
for tc in range(1, TC+1):
    tc = int(input())
    BRD = [input() for _ in range(100)]

    for i in range(100):
        for j in range(100):
            BRD[i][j]

    print(BRD)