# 레벨2 2007. 패턴 마디의 길이 
import sys
sys.stdin = open("test01.txt", "r")
 
TC = int(input())
for tc in range(1, TC+1):
    sentence = input()

    min_V = 99999
    for i in range(1, 10):
        if sentence[0:i] == sentence[i:i*2]:
            min_V = len(sentence[0:i])

    print(min_V) 

    