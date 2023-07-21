# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    answer = []
    dic_list = []
    dic = {}
    for i,word in enumerate(record):
        dic_list.append(word.split())
        dic[dic_list[i][1]] = dic_list[i][-1]
    for i,word in enumerate(dic_list):
        if dic_list[i][0] == "Enter":
            answer.append(dic[dic_list[i][1]] + '님이 들어왔습니다.')
        elif dic_list[i][0] == "Leave":
            answer.append(dic[dic_list[i][1]] + '님이 나갔습니다.')
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
