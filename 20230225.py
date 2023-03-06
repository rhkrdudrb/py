# https://school.programmers.co.kr/learn/courses/30/lessons/120902
# my_string은 "3 + 5"처럼 문자열로 된 수식입니다. 문자열 my_string이 매개변수로 주어질 때, 수식을 계산한 값을 return 하는 solution 함수를 완성해주세요.

# 제한사항
# 연산자는 +, -만 존재합니다.
# 문자열의 시작과 끝에는 공백이 없습니다.
# 0으로 시작하는 숫자는 주어지지 않습니다.
# 잘못된 수식은 주어지지 않습니다.
# 5 ≤ my_string의 길이 ≤ 100
# my_string을 계산한 결과값은 1 이상 100,000 이하입니다.
# my_string의 중간 계산 값은 -100,000 이상 100,000 이하입니다.
# 계산에 사용하는 숫자는 1 이상 20,000 이하인 자연수입니다.
# my_string에는 연산자가 적어도 하나 포함되어 있습니다.
# return type 은 정수형입니다.
# my_string의 숫자와 연산자는 공백 하나로 구분되어 있습니다.
# 입출력 예
# my_string	result
# "3 + 4"	7
# 입출력 예 설명
# 입출력 예 #1

# 3 + 4 = 7을 return 합니다. -3 + 4 -1 +2
# "3 + 4".split() => ["3", "+", "4"]
def solution(my_string):
    tokens = my_string.split() # [num1, op, num2, op2, num3, op3, ...]
    answer = int(tokens[0])
    sum = answer
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = tokens[i+1]   
        if op == "+":
            sum += int(num)   
        elif op == "-":
            sum -= int(num)
    return sum
# print(solution("3 + 4 + 5")) #12
# print(solution("3 + 4 - 5")) #2
# print(solution("1 - 20 + 30 - 4")) #7

# https://school.programmers.co.kr/learn/courses/30/lessons/120866
# 다음 그림과 같이 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
# image.png
# 지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
# 지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# board는 n * n 배열입니다.
# 1 ≤ n ≤ 100
# 지뢰는 1로 표시되어 있습니다.
# board에는 지뢰가 있는 지역 1과 지뢰가 없는 지역 0만 존재합니다.
# 입출력 예
# board	result
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]	16
# [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]	13
# [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]	0
# 입출력 예 설명
# 입출력 예 #1

# (3, 2)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선 총 8칸은 위험지역입니다. 따라서 16을 return합니다.
# 입출력 예 #2

# (3, 2), (3, 3)에 지뢰가 있으므로 지뢰가 있는 지역과 지뢰와 인접한 위, 아래, 좌, 우, 대각선은 위험지역입니다. 따라서 위험지역을 제외한 칸 수 13을 return합니다.
# 입출력 예 #3

# 모든 지역에 지뢰가 있으므로 안전지역은 없습니다. 따라서 0을 return합니다.

# [[1,2,3], (0,0) -> (0,1)
# [4,5,6],]
# row, col
def solution2(board):
    answer = 0 
    R = len(board)
    C = len(board[0])
    for r in range(len(board)):
        for c in range(len(board[c])):
            if board[r][c] == 1:
                for dr, dc in [(-1, 0),(-1,-1),(-1,1),(1,0),(0,-1),(0,1),(1,1),(1,-1)]:
                    nr= r + dr # nr, nc는 이웃점들의 실제 좌표
                    nc= c + dc
                    if 0 <= nr < R and 0 <= nc < C: # board를 넘어가지 않는지 체크
                        if board[nr][nc] != 1:
                            board[nr][nc] = 2
        #     print(board[x][y], end=' ')
        # print() 
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] < 1:
                answer += 1
            print(board[x][y], end=' ')
        print()    
    return answer
# def solution(board):
#     answer = 0 
#     bigr = len(board)
#     bigc = len(board[0])
#     for row in range(len(board)):
#         for column in range(len(board[row])):
#             if board[row][column] == 1:
#                 for dr, dc in [(-1, 0),(-1,-1),(-1,1),(1,0),(0,-1),(0,1),(1,1),(1,-1)]:
#                     nr= row + dr # nr, nc는 이웃점들의 실제 좌표
#                     nc= column + dc
#                     if 0 <= nr < bigr and 0 <= nc < bigc: # board를 넘어가지 않는지 체크
#                         if board[nr][nc] != 1:
#                             board[nr][nc] = 2
#         #     print(board[x][y], end=' ')
#         # print() 
#     for x in range(len(board)):
#         for y in range(len(board[x])):
#             if board[x][y] < 1:
#                 answer += 1
#             print(board[x][y], end=' ')
#         print()    
#     return answer
# print(solution2([[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]))
# 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0
# 0, 1, 1, 1, 0 
# 0, 1, 1, 1, 0 
# 0, 1, 1, 1, 0 
# ---------------------------
# 0, 0, 0, 0, 0
# 0, 0, 0, 0, 0
# 0, 1, 1, 1, 1 
# 0, 1, 1, 1, 1
# 0, 1, 1, 1, 1 

[
    [1,2,3],
    [4,5,6],
    [7,8,9]]

r = c = 0
for dr, dc in [(-1, 0),(-1,-1),(-1,1),(1,0),(0,-1),(0,1),(1,1),(1,-1)]:
    nr = r + dr
    nc = c + dc
    print(nr, nc)
