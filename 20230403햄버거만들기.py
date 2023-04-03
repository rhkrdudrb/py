# https://school.programmers.co.kr/learn/courses/30/lessons/133502
def solution(ingredient):
    answer = 0
    arry =[]

    for i in range(0,len(ingredient) - 4 +1):
        arry.append(ingredient[i:4+i])
        print(arry[i])
        if arry[i] == [1,2,3,1]:
            
            # print(arry)
            answer += 1   
    # 2 2 1 2
    # 2 1 2 3
    # 1 2 3 1
    # 2 3 1 2
    # 3 1 2 3
    # 1 2 3 1
    
    return answer
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))