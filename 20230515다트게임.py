# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    # print(3**1)
    # print(3**2)
    # print(3**3)
    for i in range(len(dartResult)):
        if dartResult[i] == 'S':
            answer +=int(dartResult[i-1]) ** 1
        elif dartResult[i] == 'D':
            answer +=int(dartResult[i-1]) ** 2
        elif dartResult[i] == 'T':
            answer +=int(dartResult[i-1]) ** 3
        elif dartResult[i] == '*':
            answer +=answer * 2
        elif dartResult[i] == '#':
            answer +=answer * -1
        print(answer)
# and dartResult[i+1] in '*#'
    return answer
print(solution("1S2D*3T")) #37	11 * 2 + 22 * 2 + 33
print(solution("1D2S#10S"))#9	12 + 21 * (-1) + 101
print(solution("1D2S0T"))  #3	12 + 21 + 03
print(solution("1S*2T*3S"))#23	11 * 2 * 2 + 23 * 2 + 31
print(solution("1D#2S*3S"))#5	12 * (-1) * 2 + 21 * 2 + 31
print(solution("1T2D3D#")) #-4	13 + 22 + 32 * (-1)
print(solution("1D2S3T*")) #59	12 + 21 * 2 + 33 * 2


