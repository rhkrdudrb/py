# https://school.programmers.co.kr/learn/courses/30/lessons/161989
def solution(n, m, section):
    answer = 0
    arry,answer = meter(m,section[0],answer)
    while True:
        if arry[-1] > section[-1]:
            break
        else:
            arry,answer = meter(m,arry[-1] + 1,answer)
            if arry[-1] == section[-1]:
                break
    return answer
def meter(m,num,answer):
    arry =[]
    for i in range(m):
        arry.append(num+i)
    answer +=1
    return arry,answer

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