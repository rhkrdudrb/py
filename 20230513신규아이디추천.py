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
def step3(s): #".bat.y.abcdefghijklm"
    answer = ''
    for i in range(len(s)):
        if len(s) -1 == i:
            answer += s[i]
            break
        # if not (s[i] =='.' and s[i] == s[i+1]): #, and -> or, or -> and
        if s[i] !='.' or s[i] != s[i+1]:
            answer += s[i]
    return answer
def step4(s):
    answer = ''
    for i,letter in enumerate(s):
        if (i != 0 or letter != '.') and (i != len(s)-1 or letter != '.') :
            answer += letter
    return answer
def step5(s):
    if len(s) == 0:
        return "a"
    return s
def step6(s):
    answer = ''
    if len(s) >= 16:
        answer = s[:15]
        if answer[-1] == '.' :
            answer = s[:14]
    else:
        return s
    return answer
def step7(s):
    answer = s
    if len(s) <= 2:
        while len(answer) != 3:
            answer += s[-1]
    else:
        return s
    return answer
print(solution("...!@BaT#*..y...abcdefghijklm...."))
print(solution("=.="))
print(solution("z-+.^."))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))

