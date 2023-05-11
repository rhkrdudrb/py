# https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    answer = ''
    table = {"A":0,"C":0,"F":0,"J":0,"M":0,"N":0,"R":0,"T":0}    
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    for i in range(len(choices)):
        if choices[i] in score:
            if choices[i] <= 4:
                if survey[i][0] in table:
                    table[survey[i][0]] += score[choices[i]]
            else:
                if survey[i][1] in table:
                    table[survey[i][1]] += score[choices[i]]
    
    min_value = min(table.values())
    max_value = max(table.values())
    print(dict(sorted(table.items(), key=lambda x: x[1])))
    # value 값으로 정렬후 min값이 0이면 
    # while len(answer) !=4:
    sorted(table.items(), key=lambda x: x[1])
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))

    
