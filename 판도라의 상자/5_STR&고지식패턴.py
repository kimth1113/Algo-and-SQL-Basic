# # 문자열 메소드
line = '안녕하세요'

line.replace('세', '시') # replace()
line.split('하') # split()
line.find('녕') # find()

# isalpha, isdigit
password = 'abcde'
for i in password:
    if i.isalpha(): # 만약 i가 문자라면 isalpha()
    if i.isdigit(): # 만약 i가 숫자라면 isdigit()

# ord: str 문자를 아스키코드(int)로
# chr: 아스키 코드를 str 문자로

# atoi
def atoi(num_str): # str을 int로
    #최종 값을 담을 변수
    value = 0

    for i in range(len(num_str)):
        value *= 10
        value += ord(num_str[i]) - ord('0')

    return value

# itoa
def itoa(number):
    str_number = ''
    while number > 0:
        num = number % 10
        number //= 10
        num_ord = ord('{}'.format(num))
        str_number += chr(num_ord)

    result = ''
    for i in range(len(str_number)-1, -1, -1):
        result += str_number[i]

    return result

# print(itoa(12345678910))

# 고지식한 패턴 검색
p = 'is'
t = 'This is a book~!'
M = len(p)
N = len(t)

def BruteForce(p, t):
    i = 0 # t의 인덱스
    j = 0 # p의 인덱스
    while j < M and i < N:
        if t[i] != p[j]:
            i -= j # 중간에 틀리면 다시 처음으로
            j = -1
        i += 1
        j += 1
    if j == M: return i-M # 검색 성공
    else: return -1