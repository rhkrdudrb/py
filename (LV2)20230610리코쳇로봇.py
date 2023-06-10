# https://school.programmers.co.kr/learn/courses/30/lessons/169199

def solution(board):
    R = len(board)
    C = len(board[0])

    def find_start():
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'R':
                    return i,j
                
    r, c = find_start()
    up = (r-1,c)
    for i in board:

    # up: r,c -> 
    for i in board:
        

print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
# ["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]	7
# [".D.R", "....", ".G..", "...D"]	-1

"...D..."
".D.G.R."
"....D.D"
"D....D."
"..D...."

# R: (1, 6) -> (0, 6)
# R: (1, 5) -> (0, 5)
# (r, c) -> (r-1, c)

# https://school.programmers.co.kr/learn/courses/30/lessons/172928
def solution(park, routes):
    R = len(board)
    C = len(board[0])
    board = create_board(park)
    for i in range(R):
        for j in range(C):
            if board[i][j] == 'S':
                r,c = i,j
    move = {"E":(0,1),"W":(0,-1),"S":(1,0),"N":(-1,0)} #동서남북 딕셔너리
    for route in routes:
        ewsn,move = route.split()



        

def create_board(park):
    board = []
    for s in park:
        s =list(s)
        board.append(s)
    return board
def board_start()
print(solution(["SOO","OOO","OOO"],["E 2","S 2","W 1"]))