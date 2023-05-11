# https://school.programmers.co.kr/learn/courses/30/lessons/118666
def solution(survey, choices):
    answer = ''
    table = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    # 질문의 성격 유형점수 합한값
    for i in range(len(choices)):
        if choices[i] in score:
            if choices[i] <= 4:
                if survey[i][0] in table:
                    table[survey[i][0]] += score[choices[i]]
            else:
                if survey[i][1] in table:
                    table[survey[i][1]] += score[choices[i]]
    # 출력 
    table_key = list(table.keys())
    
    for i in range(0, len(table), 2):
        if table[table_key[i]] > table[table_key[i+1]]:
            answer += table_key[i]
        elif table[table_key[i]] < table[table_key[i+1]]:
            answer += table_key[i+1]
        else:
            answer += min(table_key[i], table_key[i+1])
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))

    
