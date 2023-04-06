# def solution(ingredient):
#     answer = 0
#     y=0
#     while True:    
#         if not ingredient[y:4+y] or len(ingredient[y:4+y]) !=4:     
#             break
#         # print(ingredient[y:4+y])
#         if ingredient[y:4+y] == [1,2,3,1]:
#             del ingredient[y:4+y]
#             y = 0
#             answer += 1 
#             continue
#         y+=1   
def solution(ingredient):
    answer = 0
    y=0
    lastOne = []
    while True:    
        lastOne = ingredient[y:4+y]
        if not lastOne or len(lastOne) !=4:     
            break
        if lastOne[-1] == 1:
            if lastOne == [1,2,3,1]:
                del ingredient[y:4+y]
                y = 0
                answer += 1 
                continue
        y+=1    
    return answer
