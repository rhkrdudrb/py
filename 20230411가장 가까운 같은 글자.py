# https://school.programmers.co.kr/learn/courses/30/lessons/142086
def solution(s):
    answer = []
    arry =list(set(s))
    y = 0
    print(arry)
    while len(s) != len(answer):
        for i in range(len(s)):
            if s[i] == arry[y]:
                answer.append(i)  
        y+=1
        print(answer)
    return answer
print(solution("banana"))
