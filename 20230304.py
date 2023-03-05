# https://school.programmers.co.kr/learn/courses/30/lessons/120896
# 문자열 s가 매개변수로 주어집니다. s에서 한 번만 등장하는 문자를 사전 순으로 정렬한 문자열을 return 하도록 solution 함수를 완성해보세요. 
# 한 번만 등장하는 문자가 없을 경우 빈 문자열을 return 합니다.

# 제한사항
# 0 < s의 길이 < 1,000
# s는 소문자로만 이루어져 있습니다.
# 입출력 예
# s	result
# "abcabcadc"	"d"
# "abdc"	"abcd"
# "hello"	"eho"
# 입출력 예 설명
# 입출력 예 #1

# "abcabcadc"에서 하나만 등장하는 문자는 "d"입니다.
# 입출력 예 #2

# "abdc"에서 모든 문자가 한 번씩 등장하므로 사전 순으로 정렬한 "abcd"를 return 합니다.
# 입출력 예 #3

# "hello"에서 한 번씩 등장한 문자는 "heo"이고 이를 사전 순으로 정렬한 "eho"를 return 합니다.
# 한개만 등장한거 뽑고 사전순 정렬 글지별로 얼마나 등장한지?
# 글자 -> 카운트
from collections import defaultdict

def solution(s):
    answer = ''
    let2cnt = defaultdict(int)
    for letter in s:
        let2cnt[letter] += 1
    print(let2cnt)
    for k, v in let2cnt.items():
        if v ==1 :
            answer += k
    return ''.join(sorted(answer))
# print(solution("hello"))

# https://school.programmers.co.kr/learn/courses/30/lessons/120894
# 영어가 싫은 머쓱이는 영어로 표기되어있는 숫자를 수로 바꾸려고 합니다. 문자열 numbers가 매개변수로 주어질 때, 
# numbers를 정수로 바꿔 return 하도록 solution 함수를 완성해 주세요.

# 제한사항
# numbers는 소문자로만 구성되어 있습니다.
# numbers는 "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine" 들이 공백 없이 조합되어 있습니다.
# 1 ≤ numbers의 길이 ≤ 50
# "zero"는 numbers의 맨 앞에 올 수 없습니다.
# 입출력 예
# numbers	result
# "onetwothreefourfivesixseveneightnine"	123456789
# "onefourzerosixseven"	14067
# 입출력 예 설명
# 입출력 예 #1

# "onetwothreefourfivesixseveneightnine"를 숫자로 바꾼 123456789를 return합니다.
# 입출력 예 #1

# "onefourzerosixseven"를 숫자로 바꾼 14067를 return합니다.
def solution1(numbers):
    numbers = numbers.replace('zero','0')
    numbers = numbers.replace('one','1')
    numbers = numbers.replace('two','2')
    numbers = numbers.replace('three','3')
    numbers = numbers.replace('four','4')
    numbers = numbers.replace('five','5')
    numbers = numbers.replace('six','6')
    numbers = numbers.replace('seven','7')
    numbers = numbers.replace('eight','8')
    numbers = numbers.replace('nine','9')
    return int(numbers)
print(solution1("oneoneoneoneonethreesixseveneightnineoneoneoneone"))

# https://school.programmers.co.kr/learn/courses/30/lessons/120821
# reverse(역순) 함수 씀
# def solution2(num_list):
#     num_list.reverse()
#     return num_list
# 안씀
def solution2(num_list):
    answer = ''
    for i in range(len(num_list)):
        answer = num_list[i]
        num_list[i] = num_list[len(num_list)-i-1]     
        num_list[len(num_list)-i-1] = answer
        if num_list[len(num_list)-i-1] == num_list[i]:
            break
    print(num_list)
    return answer
print(solution2([1, 2, 3, 4, 5]))


# https://school.programmers.co.kr/learn/courses/30/lessons/120822
def solution3(my_string):
    answer = ''
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/120854
def solution4(strlist):
    answer = []
    return answer