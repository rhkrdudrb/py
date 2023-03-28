# https://school.programmers.co.kr/learn/courses/30/lessons/172928?language=python3

def solution(park, routes):
    #판 만들기
    answer = []
    op2n ={}
    for letter in park:
        letter = (' ').join(letter)
        letter = letter.split()
        answer.append(letter) 
    for route in routes:
        op,n = route.split()
        op2n[op] = n
    print(op2n.keys())
    # 2
    R = len(answer)
    C = len(answer[0])
    for i in range(len(answer)):
        for j in range(len(answer[i])):
            print(answer[i][j], end='')
            if answer[i][j] == 'S':
                for op in op2n.keys():
                    if op == 'E':
                        for dr, dc in [(0, int(op2n[op]))]:
                            nr = i + dr
                            nc = j + dc
                            if 0 <= nr < R and 0 <= nc < C: # board를 넘어가지 않는지 체크
                                if answer[nr][nc] != 'X':
                                    answer[nr][nc] = 2
                    elif op == 'W':
                        for dr, dc in [(0, int(op2n[op]))]:
                            nr = i + dr
                            nc = j + dc
                            if 0 <= nr < R and 0 <= nc < C: # board를 넘어가지 않는지 체크
                                if answer[nr][nc] != 'X':
                                    answer[nr][nc] = 1                
        print('')
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