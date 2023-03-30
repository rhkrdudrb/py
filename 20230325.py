# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3
def solution(park, routes):
    answer = []
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
    #판 만들기
    for letter in park:
        letter = (' ').join(letter)
        letter = letter.split()
        answer.append(letter) 
    # 시작점
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            if answer[i][j] == 'S':
                x,y = i,j 
    # 판경계
    R = len(answer)
    C = len(answer[0])
    #하나씩 돌려가면서 x체크및 박스 크기 벗어나는 곳 체크            
    for route in routes:
        dr,dc = move[route[0]] # 동서남북
        new_r,new_c = x,y # new_r,new_c : 하나씩 돌려가면서 체크 하며 저장할 값
        for i in range(int(route[2])): 
            if 0<=new_r+dr<R and 0<=new_c+dc<C and answer[new_r+dr][new_c+dc] != "X":
                new_r,new_c = new_r+dr,new_c+dc
            else: # 아니라면 처음 위치로(초기화)
                new_r,new_c = x,y
                break
        x,y = new_r,new_c # 위치 업데이트         
    return x,y
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
