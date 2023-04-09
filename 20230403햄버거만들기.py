def solution(ingredient):
    answer = 0
    y=0
    stack = [] # 1, 2, 3, 1
    for el in ingredient:
        stack.append(el)
        if el == 1 and len(stack) >= 4:
            if stack[-4:] == [1,2,3,1]:
                answer += 1
                for _ in range(4):
                    stack.pop()

    return answer
# def solution(ingredient):
#     answer = 0
#     y=0
#     lastOne = []
#     while True:    
#         lastOne = ingredient[y:4+y]
#         if not lastOne or len(lastOne) !=4:     
#             break
#         if lastOne[-1] == 1:
#             if lastOne == [1,2,3,1]:
#                 del ingredient[y:4+y]
#                 y = 0
#                 answer += 1 
#                 continue
#         y+=1    
#     return answer
# stack

12 1231 31



