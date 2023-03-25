# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3

def solution(park, routes):
    #판 만들기
    #
    answer = []
    return answer
# S : 시작 지점
# O : 이동 가능한 통로
# X : 장애물
# op는 다음 네 가지중 하나로 이루어져 있습니다.
# N : 북쪽으로 주어진 칸만큼 이동합니다.
# S : 남쪽으로 주어진 칸만큼 이동합니다.
# W : 서쪽으로 주어진 칸만큼 이동합니다.
# E : 동쪽으로 주어진 칸만큼 이동합니다.
print(solution(park, routes))
# park routes
# ["SOO","OOO","OOO"]	["E 2","S 2","W 1"]	[2,1]
# ["SOO","OXX","OOO"]	["E 2","S 2","W 1"]	[0,1]
# ["OSO","OOO","OXO","OOO"]	["E 2","S 3","W 1"]	[0,0]