# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    dartResult = dartResult.replace("10","A")
    dartdict = {'S':1,'D':2,'T':3}
    print(dartdict)
    answer=[]
    for i in range(len(dartResult)):
        if dartResult[i] in 'SDT':
            if dartResult[i-1] =='A':                
                answer.append(10**dartdict[dartResult[i]])
            else:
                answer.append(int(dartResult[i-1])**dartdict[dartResult[i]])
        elif dartResult[i] =='*':
            answer[-1] *= 2
            if len(answer) >= 2:
                answer[-2] *= 2
        elif dartResult[i] =='#':
            answer[-1] *= -1
    print(answer)
    return sum(answer)
#어떤예제가 안되는걸까?
    # 문자열 분리
#     answer=[]
#     score
    # for i,letter in enumerate(dartResult):
    #     if letter not in '*#':
    #         score+=letter
    # j=0
    # # S,D,T 제곱
    # print(score)
    # for i in range(len(score)): 
    #     if score[i] =='S':
    #         answer.append(int(score[j:i]))
    #         j = i +1
    #     elif score[i] =='D':
    #         answer.append(int(score[j:i])**2)
    #         j = i +1
    #     elif score[i] =='T':
    #         answer.append(int(score[j:i])**3)
    #         j = i +1
    # # 스타상 아차상 계산   
    # for i,letter in enumerate(dartResult):
    #     if letter == '#':
    #         answer[int(i/2 -1)] *= -1
    #     elif letter == '*':
    #         answer[int(i/2 -1)] *= 2
    #         if 0 <= int(i/2 -1)-1:
    #             answer[int(i/2 -1)-1] *= 2
print(solution("1S2D*3T")) #37	11 * 2 + 22 * 2 + 33
print(solution("1D2S#10S"))#9	12 + 21 * (-1) + 101
print(solution("1D2S0T"))  #3	12 + 21 + 03
print(solution("1S*2T*3S"))#23	11 * 2 * 2 + 23 * 2 + 31
print(solution("1D#2S*3S"))#5	12 * (-1) * 2 + 21 * 2 + 31
print(solution("1T2D3D#")) #-4	13 + 22 + 32 * (-1)
print(solution("1D2S3T*")) #59	12 + 21 * 2 + 33 * 2


