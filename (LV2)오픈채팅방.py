# https://school.programmers.co.kr/learn/courses/30/lessons/42888
# ----------------------V0.2(정답)--------------------------------
def solution(record):
    answer = []
    dic_list = []
    dic = {} # id2name
    for i,word in enumerate(record):
        words = word.split()
        dic_list.append(words)                       # record 공백기준 배열 아래 단락 for문 기준
        list_dic = words # key2value
        if list_dic[0] =="Enter" or list_dic[0] =="Change": # 들어오고 변경되는부분일경우만 (떠나는 경우는 들어와야 떠날수 있어서 굳 이 필요업음)
            dic[list_dic[1]] = list_dic[-1]                 # 딕셔너리 - > ID(key) : name(value)
    for i,word in enumerate(dic_list):
        if dic_list[i][0] == "Enter":
            answer.append(dic[dic_list[i][1]] + '님이 들어왔습니다.')
        elif dic_list[i][0] == "Leave":
            answer.append(dic[dic_list[i][1]] + '님이 나갔습니다.')
    return answer
# ----------------------V0.1--------------------------------
# def solution(record):
#     answer = []
#     dic_list = []
#     dic = {}
#     for i,word in enumerate(record):
#         dic_list.append(word.split())
#         dic[dic_list[i][1]] = dic_list[i][-1]
#     for i,word in enumerate(dic_list):
#         if dic_list[i][0] == "Enter":
#             answer.append(dic[dic_list[i][1]] + '님이 들어왔습니다.')
#         elif dic_list[i][0] == "Leave":
#             answer.append(dic[dic_list[i][1]] + '님이 나갔습니다.')
#     return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
