# https://school.programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    answer = step7(step6(step5(step4(step3(step2(step1(new_id)))))))
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

def step3(s): #".bat.y.abcdefghijklm.."
    answer = ''
    for i in range(len(s)-1): 
        # if not (s[i] =='.' and s[i] == s[i+1]): #, and -> or, or -> and
        if s[i] !='.' or s[i] != s[i+1]:
            answer += s[i]
    answer += s[-1]
    return answer

def step4(s): # 양끝의 . 삭제 .a.b.c. >> a.b.c / aa.b.cc >> aa.b.cc
    answer = ''
    # idx 0
    if s and s[0] != '.': # s : ''
        answer = s[0] 
    answer += s[1:len(s) - 1]
    # for i in range(1,len(s)-1):
    #         answer += s[i]
    if s and s[-1] != '.': # s : ''
        answer += s[-1] 
    # for i,letter in enumerate(s):
    #     if (i != 0 or letter != '.') and (i != len(s)-1 or letter != '.') :
    #         answer += letter
    # idx = len(s) - 1
    return answer

def step5(s):
    if len(s) == 0:
        return "a"
    return s
# new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
    #  만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
def step6(s):
    if len(s) < 15:
        return s
    answer = s[:15]
    if answer[-1] == '.' :
        answer = s[:14]
    return answer

def step7(s): # ab -> abb, bbb
    if len(s) > 2:
        return s 
    answer = s
    while len(answer) != 3:
        answer += s[-1]
    return answer

print(solution("...!@BaT#*..y...abcdefghijklm...."))
print(solution("=.="))
print(solution("z-+.^."))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

