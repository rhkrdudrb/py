# https://school.programmers.co.kr/learn/courses/30/lessons/43165

# homework: https://school.programmers.co.kr/learn/courses/30/lessons/1844
#           solution([1,1,1], 1) 이거 다 펼쳐보기
# recursion
def solution(numbers, target):
    if not numbers: # numbers == []
        # base case        
        if target == 0:
            return 1
        else:
            return 0
    return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])
    # (+numbers[0]인 경우의 수) +  (-numbers[0]인 경우의 수)
    
# [1,1,1,1,1] , 3
# + 1, ([1,1,1,1] , 3 - 1) / -1, ([1,1,1,1], 3 + 1)



# +1 (1,1,1,1,1), 3 - 1 = 3
# [1,1,1,1,1] = 3
# 1 + [1,1,1,1] = 3
# [1,1,1,1] = 3 - 1
# [1,1,1] = 3 -1 -1
# [1,1] = 3 -1 -1 -1
# [1] =3 -1 -1 -1 -1  
# 0 = 3 -1 -1 -1 -1 -1

# + 1 + 1 + 1 + 1 + 1 != 3
# 1 = 3 - 1 -1 -1 -1
# 1 - 1 = (3 - 1 - 1 -1 - 1) - 1 
# 0 = 3 - 1 - 1 -1 -1 -1

# solution([1, 1, 1, 1, 1], 3)
# = solution([1,1,1,1], 2) + solution([1,1,1,1], 4)

# solution([1,1,1,1], 2) 
# = solution([1,1,1], 1) 2-1 

# solution([1,1,1], 1) 
# = solution([1,1], 0)  

# solution([1,1], 0) 
# = solution([1], -1)

# solution([1], -1) 
# = solution([], -2) 

# 3-1 ->2   3+1 -> 4
# [1, 1, 1, 1], 3 
# 3-1 -> 2  3+1 -> 4
# [1, 1, 1], 3 
# 3-1 -> 2  3+1 -> 4





# [4, 1, 2, 1] # 4

# 4 -1 + 2 - 1 = 4

