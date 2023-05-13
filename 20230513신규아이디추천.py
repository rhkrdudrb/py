# https://school.programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    answer = ''
    return answer
    # lower()

def step1(s):
    return s.lower()

def step2(s):
    answer = ''
    # letter = 'cbc'
    # letter.isalpha() >> 영어 알파벳
    # 'a' <= letter <= 'z', 1 < 3
    # '-_' in '-_.' : True
    for letter in s:
        if letter.isalpha() or letter.isdigit() or letter in '-_.': #  letter == '-' or letter == '_' or letter == '.': # 소문자, . -, _ 이면 담는다
            answer += letter
    return answer

def step3(s):
    answer = ''
    for i in range(len(s)):
        # if not (s[i] =='.' and s[i] == s[i+1]): , and -> or, or -> and
        if s[i] !='.' or s[i] != s[i+1]:
            answer += s[i]
    return answer


def step4(s):
    return s

def step5(s):
    return s

def step6(s):
    return s

def step7(s):
    return s