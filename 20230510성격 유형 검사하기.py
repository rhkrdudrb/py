# https://school.programmers.co.kr/learn/courses/30/lessons/118666
#외움 다시 보기
def solution(survey, choices):
    answer = ''
    table =  defaultdict(int)
    table_arry = [('R','T'),('J','M'),('C','F'),('A','N')]
    for i in range(len(choices)):
        if choices[i] > 4:
            table[survey[i][1]] += choices[i] -4
        else:
            table[survey[i][1]] += 4 - choices[i]
    for i in table_arry:
        if table[i[0]] >= table[i[1]]:
            answer += i[0]
        else:
            answer += i[1]
    return answer
from collections import defaultdict

#     라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)
# ["AN", "CF", "MJ", "RT", "NA"]	[5, 3, 2, 7, 5]	"TCMA"
# AN , 5 : N, 1
# CF, 3 : C, 1
# MJ, 2 : M, 2
# 매우 비동의	네오형 3점
# 비동의	네오형 2점
# 약간 비동의	네오형 1점
# 모르겠음	어떤 성격 유형도 점수를 얻지 않습니다
# 약간 동의	어피치형 1점 
# 동의	어피치형 2점 
# 매우 동의	어피치형 3점
# 0330 ~ 0408 외우기 + 스텍문제 + 성격유형검사 다외우기
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
print(solution(["TR", "RT", "TR"],[7, 1, 3]))




















def solution1(survey, choices):
    answer = ''
    table = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = {1 : 3, 2 : 2, 3 : 1, 4 : 0, 5 : 1, 6 : 2, 7 : 3}
    # 질문의 성격 유형점수 합한값
    for i in range(len(choices)):
        if choices[i] in score:
            # 1,2,3,4 -> 1,2,3,4
            # 5,6,7 -> 1,2,3
            # value = choices[i] % 4
            idx = (choices[i] + 1) // 4
            table[survey[i][idx]] += score[choices[i]]
            # if choices[i] <= 4:
            #     if survey[i][0] in table:
            #         table[survey[i][0]] += score[choices[i]]
            # else:
            #     if survey[i][1] in table:
            #         table[survey[i][1]] += score[choices[i]]
    # 출력 
    table_key = list(table.keys())
    # table_key = ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    # ['A', 'C', 'F', 'J', 'M', 'N', 'R', 'T']
    
    for i in range(0, len(table), 2):
        if table[table_key[i]] > table[table_key[i+1]]:
            answer += table_key[i]
        elif table[table_key[i]] < table[table_key[i+1]]:
            answer += table_key[i+1]
        else:
            answer += min(table_key[i], table_key[i+1])
    return answer
# print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))
# print(solution(["TR", "RT", "TR"],[7, 1, 3]))

    
# 1번 지표	라이언형(R), 튜브형(T)
# 2번 지표	콘형(C), 프로도형(F)
# 3번 지표	제이지형(J), 무지형(M)
# 4번 지표	어피치형(A), 네오형(N)

