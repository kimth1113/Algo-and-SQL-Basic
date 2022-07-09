# <map, int>
# 정수 => 문자열 int()
# 문자열 => 정수 str()

# lst = ['1', '2', '3']
# alst = '123'
# for a in alst:
#     print(a)

# for a in lst:
#     print(a)

# 리스트 => 문자열: list(alst)
# 문자열 => 리스트: ''.join(lst)

# ord 외 내장함수 쓰기 않기
# 연습1) reverse 함수 만들기 
def reverse_str(words):
    new_words = []
    for i in range(len(words)-1, -1, -1):
        new_words += words[i]
    
    new_words = ''.join(new_words)
    
    return new_words
    
# 연습2) itoa 함수 만들기

def itoa(numbers):
    new_numbers = []
    while numbers > 0:
        new_numbers += [numbers % 10]
        numbers = numbers // 10
    
    new2_numbers = []
    for i in range(len(new_numbers)-1, -1, -1):
        new2_numbers += [new_numbers[i]]
    
    str_numbers = []
    for i in new2_numbers:
        
    

    return new2_numbers

