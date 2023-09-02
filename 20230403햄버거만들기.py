# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0
    nums = []  # 1231
    for num in range(ingredient):
        nums.append(num)
        if num == 1 and len(nums) >=4:  
            if nums[-4:] == [1,2,3,1]:
                answer+=1
                # nums = nums[:-4]
                for _ in range(4):
                    nums.pop()
    return answer
# toks = toks[:i-1] + [tok_result] + toks[i+2:] #[]
nums = [1,1,2,3,1,2,3,1] # >> [1,1,2,3]
nums[:4]
nums[:-4] #뒤에 4개

answer = 0
nums= []
for num in range(ingredient):
    nums.append(num)
    if num == 1 and len(nums) >= 4:
        if nums[-4:] ==[1,2,3,1]:
            answer+=1
            for _ in range(4):
                nums.pop












# def solution(ingredient):
#     answer = 0
#     y=0
#     stack = [] # 1, 2, 3, 1
#     for el in ingredient:
#         stack.append(el)
#         if el == 1 and len(stack) >= 4:
#             if stack[-4:] == [1,2,3,1]:
#                 answer += 1
#                 for _ in range(4):
#                     stack.pop()

#     return answer
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

# 12 1231 31



