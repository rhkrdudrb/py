# https://school.programmers.co.kr/learn/courses/30/lessons/161989
# https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    y = 0
    arry = []
    while len(section) > 0:
        for i in range(m):
            arry.append(section[y] + y +i)
        delete = list(set(arry) & set(section))
        for dnum in delete:
            section.remove(dnum)
        answer += 1
    return answer
# print(solution(8,4,[2,3,6]))
# print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))
# 8, 4
# 2,3,6
# 2 3 4 5 6
# X X X X
#         X X X X 

# 5, 4
# 1, 3
# 1 2 3 4 5
# X X X X 

# 4 ,1
# 1 2 3 4
# 1 2 3 4 
# X
#   X
#     X
#       X

# print(solution(8,4,[2,3,6]))
# print(solution(5,4,[1,3]))
print(solution(4,1,[1,2,3,4]))
# 8, 4
# 2,3,6
# 2 3 4 5 6
# X X X X
#         X X X X 

# 5, 4
# 1, 3
# 1 2 3 4 5
# X X X X 

# 4 ,1
# 1 2 3 4
# 1 2 3 4 
# X
#   X
#     X
#       X
