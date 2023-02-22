# 최대값 만들기
# numbers	result
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744
# 입출력 예 설명
# 입출력 예 #1

# 두 수의 곱중 최댓값은 4 * 5 = 20 입니다.
# 입출력 예 #1

# 두 수의 곱중 최댓값은 31 * 24 = 744 입니다.
def solution1(numbers):
    answer = numbers.sort()[-1] #최고값
    nummax = numbers.sort()[-2] #두번째값
    return answer * nummax
#sort 쓰지않고 풀이
def solution2(numbers):
    answer = max(numbers)   #가장큰값
    numarray = [num for num in numbers if num != answer]  #가장큰값 버림 이유 max값이 2개이면 런타임에러남
    townum = [num for num in numarray if num == max(numarray)] #2번째 큰 값
    if len(numarray) == 0:
        return max(numbers) * max(numbers)
    else:
        return answer * max(townum)
# max 안쓰고 풀기 
# def solution(numbers):
#     max = maxnum(numbers) #최고값
#     array = [num for num in numbers if num != max]
#     print(len(array))
#     if len(array) == 0:
#         return max * max 
#     max2 =(maxnum(array))
#     return max * max2
def maxnum(nummax):
    if len(nummax) == 0:
        return nummax[0]
    max = nummax[0]
    min = nummax[0]
    index = nummax[0]
    for num in nummax:
        if max < num:
            max = num
        if min < num and max < min:
            min = num
        index = num    
    return max,min    
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744
# print(maxnum([0, 31, 24, 10, 1, 9]))
print(maxnum([1, 2, 3, 4, 5]))
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 2 ≤ my_string 길이 ≤ 5
# 2 ≤ n ≤ 10
# "my_string"은 영어 대소문자로 이루어져 있습니다.
# 입출력 예
# my_string	n	result
# "hello"	3	"hhheeellllllooo"
def solution4(my_string, n):
    answer = ''
    for word in my_string:
        answer += word * n   #문자 * 숫자 된다니 신기함
    return ''.join(answer)   # 파이썬 리스트를  문자로 바꿔줌
