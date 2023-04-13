# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    result = []
    for letter in s:
        if letter not in result:
            result.append(letter)
    y = 0
    key = []
    while len(s) != len(answer):
        for i in range(len(s)):
            if s[i] == result[y]:
                key.append(result[y])
                answer.append(i)  
        y+=1
    print(key)
    print(answer)
    return answer
print(solution("banana"))
