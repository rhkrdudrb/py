# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3

def solution(park, routes):
    #판 만들기
    answer = []
    for letter in park:
        letter = (' ').join(letter)
        letter = letter.split()
        answer.append(letter) 
    # 2
    for i in range(len(answer)):
        for j in range(len(answer[i])):
             print(answer[i][j], end='')
             if answer[i][j] == 'S':
                 answer[0][2] ='s'
        print('')
    # print(routes)
    # print(answer)
    return -1
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
# op는 다음 네 가지중 하나로 이루어져 있습니다.
# N : 북쪽으로 주어진 칸만큼 이동합니다. []
# S : 남쪽으로 주어진 칸만큼 이동합니다. []
# W : 서쪽으로 주어진 칸만큼 이동합니다. []
# E : 동쪽으로 주어진 칸만큼 이동합니다. []
print(solution(["SOO","OOO","OOO"], ["E 2","S 2","W 1"]))
# park routes
# ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# SOO
# OOO
# OOO
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# SOO
# OXX
# OOO
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]
# OSO
# OOO
# OXO
# OOO