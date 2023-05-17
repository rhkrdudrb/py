# https://school.programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    dartResultTemp = ''
    dartResultdict = {}
    k=0
    #문자열 분리
    for i,letter in enumerate(dartResult):
        if letter not in '*#':
            dartResultTemp+=letter
        else:
            dartResultdict[letter+str(k)] = i
            k+=1
    temp = []
    j=0
    # S,D,T 제곱
    for i in range(len(dartResultTemp)): 
        if dartResultTemp[i] =='S':
            temp.append(int(dartResultTemp[j:i]))
            j = i +1
        elif dartResultTemp[i] =='D':
            temp.append(int(dartResultTemp[j:i])**2)
            j = i +1
        elif dartResultTemp[i] =='T':
            temp.append(int(dartResultTemp[j:i])**3)
            j = i +1
    # 스타상 아차상 계산        
    for i in range(len(dartResultdict)):
        if '#'+str(i) in dartResultdict:
            temp[int(dartResultdict["#"+str(i)]/2 -1)] *= -1
        elif '*'+str(i) in dartResultdict:
            temp[int(dartResultdict["*"+str(i)]/2 -1)] *= 2
            if 0 <= int(dartResultdict["*"+str(i)]/2 -1) -1:
                temp[int(dartResultdict["*"+str(i)]/2 -1) -1] *= 2
    answer = sum(temp)        
    return answer
print(solution("1S2D*3T")) #37	11 * 2 + 22 * 2 + 33
print(solution("1D2S#10S"))#9	12 + 21 * (-1) + 101
print(solution("1D2S0T"))  #3	12 + 21 + 03
print(solution("1S*2T*3S"))#23	11 * 2 * 2 + 23 * 2 + 31
print(solution("1D#2S*3S"))#5	12 * (-1) * 2 + 21 * 2 + 31
print(solution("1T2D3D#")) #-4	13 + 22 + 32 * (-1)
print(solution("1D2S3T*")) #59	12 + 21 * 2 + 33 * 2


