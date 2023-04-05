# https://school.programmers.co.kr/learn/courses/30/lessons/133502
def solution(ingredient):
    answer = 0
    y=0
    for _ in range(len(ingredient)):
        if not ingredient[y:4+y] or len(ingredient[y:4+y]) !=4:     
            break
        if ingredient[y:4+y] == [1,2,3,1]:
            del ingredient[y:4+y]
            y = 0
            answer += 1 
            continue
        y+=1    
    return answer
print(solution([2, 1, 1, 2, 3, 1, 2, 3, 1]))
