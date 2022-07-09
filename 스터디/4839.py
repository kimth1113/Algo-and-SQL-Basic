import sys
sys.stdin = open('4839.txt', 'r')

def dinSearch(total, key):
    start = 1
    last = total
    result = 0
    
    while start < last:
        c = (start+last) // 2
        if c == key:
            return result
        elif c < key:
            start = c
            result += 1
        else:
            last = c
            result += 1
    return -1

TC = int(input())
for tc in range(1, TC+1):
    P, A, B = map(int, input().split())

    a_result = dinSearch(P, A)
    b_result = dinSearch(P, B)
        
    if a_result < b_result:
        print('#{} {}'.format(tc, 'A'))
    elif a_result == b_result:
        print('#{} {}'.format(tc, 0))
    else:
        print('#{} {}'.format(tc, 'B'))
            
