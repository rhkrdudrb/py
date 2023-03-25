# https://school.programmers.co.kr/learn/courses/30/lessons/155652
# 두 문자열 s와 skip, 그리고 자연수 index가 주어질 때, 다음 규칙에 따라 문자열을 만들려 합니다. 암호의 규칙은 다음과 같습니다.

# 문자열 s의 각 알파벳을 index만큼 뒤의 알파벳으로 바꿔줍니다.
# index만큼의 뒤의 알파벳이 z를 넘어갈 경우 다시 a로 돌아갑니다.
# skip에 있는 알파벳은 제외하고 건너뜁니다.
# 예를 들어 s = "akuks", skip = "wbqd", index = 5일 때, a에서 5만큼 뒤에 있는 알파벳은 
# f지만 [b, c, d, e, f]에서 'b'와 'd'는 skip에 포함되므로 세지 않습니다. 따라서 'b', 'd'를 제외하고 'a'에서 
# 5만큼 뒤에 있는 알파벳은 [c, e, f, g, h] 순서에 의해 'h'가 됩니다. 나머지 "ukks" 또한 위 규칙대로 바꾸면 "appy"가 되며
#  결과는 "happy"가 됩니다.

# 두 문자열 s와 skip, 그리고 자연수 index가 매개변수로 주어질 때 위 규칙대로 s를 변환한 결과를 return하도록 solution 함수를 완성해주세요.

# 제한사항
# 5 ≤ s의 길이 ≤ 50
# 1 ≤ skip의 길이 ≤ 10
# s와 skip은 알파벳 소문자로만 이루어져 있습니다.
# skip에 포함되는 알파벳은 s에 포함되지 않습니다.
# 1 ≤ index ≤ 20
# 입출력 예
#    s	     skip   index result
# "aukks"	"wbqd"	  5	  "happy"
# 입출력 예 설명
# 입출력 예 #1
# 본문 내용과 일치합니다.

# ord: ord('a') -> 67
# chr: chr(67) -> 'a'

def solution(s, skip, index):
    # 1. ord 활용해서 a -> bcdef
    answer = ''
    for letter in s:
        answer += oneletter(letter, skip, index) 
    # answer = oneletter('a', 'bef', 3)
    print(answer)    
    return answer
    # 1. ord 활용해서 a -> bcdef
    # 2. bcdef, skip이랑 비교해서 개수 dup를 구해서 
    # 3. bcdef -> cef, replace 쓰지말기
    # dup만큼 1번 다시
def oneletter(letter, skip, index): # 'a', 'wbqd', 5
    curr = letter # 현재 보고 있는 글자 # 'a'
    num = 0 # 몇칸 이동했는지 나타내는 카운트 # 0
    while num != index:    
        print(curr,' ',num)
        print('------------')
        curr = chr(ord(curr)+1)    
        if ord(curr) > ord('z'):
            curr = 'a'
        if curr not in skip:
            num += 1
    return curr
    # letter가 index만큼 이동한 뒤
    # return
# bef
# curr, num
# a, 0
# b, 0
# c, 1
# d, 2
# e, 2
# f, 2
# g, 3  

# wbqd
# curr, num
# a, 0 - while -> b, 0
# b, 0 - while -> c, 1
# c, 1 - while -> d, 1
# d, 1
# e, 2
# f, 3
# g, 4
# h, 5 
print(solution('aukks', 'wbqd', 5)) #> 'h')
# print(solution('zzzzzz', 'abcdefghijklmnopqrstuvwxy', 6))
