# 최대값 만들기
# numbers	result
# [1, 2, 3, 4, 5]	20
# [0, 31, 24, 10, 1, 9]	744
# 입출력 예 설명
# 입출력 예 #1

# 두 수의 곱중 최댓값은 4 * 5 = 20 입니다.
# 입출력 예 #1

# 두 수의 곱중 최댓값은 31 * 24 = 744 입니다.
def solution(numbers)
    # max(numbers) 이거 안됨..?
    answer = numbers.sort()[-1] #최고값
    nummax = numbers.sort()[-2] #두번째값
    return answer * nummax
end
# 문자열 my_string과 정수 n이 매개변수로 주어질 때, my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.

# 제한사항
# 2 ≤ my_string 길이 ≤ 5
# 2 ≤ n ≤ 10
# "my_string"은 영어 대소문자로 이루어져 있습니다.
# 입출력 예
# my_string	n	result
# "hello"	3	"hhheeellllllooo"
def solution(my_string, n):
    answer = ''
    for word in my_string:
        answer += word * n   #문자 * 숫자 된다니 신기함
    return ''.join(answer)   # 파이썬 리스트를  문자로 바꿔줌
