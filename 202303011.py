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
    answer2 = ''
    answer3 = ''
    answer4 = ''
    # for letter in s:
    #     answer += oneletter(letter, skip, index)
    answer = oneletter('a','bef', 3)
    answer2 = twoletter('a', 3)
    answer3 = threeletter('bcd', 'bef')
    answer4 = foreletter('a',answer3[1],'cd')
    print(answer)
    print('------------------------')
    print(answer2)
    print('------------------------')
    print(answer3)
    print('------------------------')
    print(answer4)
    print('------------------------')
    return answer
    # 2. bcdef, skip이랑 비교해서 개수 dup를 구해서 
    # 3. bcdef -> cef, replace 쓰지말기
    # dup만큼 1번 다시

# print(solution("aukks","wbqdgi",5))
# a, "bcdef" -> "cef" -> "cefgh" -> "cefhi" -> "h"
# u, 
def twoletter(letter, index):
    answer =''
    num = 0
    while len(answer) != index:
        cnt = 0
        for i in range(index):
            if ord(letter) +i + 1 > 122 :
                answer += chr(ord('a')+ num) 
                num += 1    
            else:
                answer += chr(ord(letter) +i +1)
    return answer  
def threeletter(letter, skip):
    answer = letter
    tmp =''
    cnt = 0
    for letter in answer:
        if letter in skip:
            cnt += 1
        else:
            tmp += letter
    answer = tmp
    print('123232132321 ',skip)            
    return [answer,cnt]

def foreletter(letter, cnt,answer):
    num = 0
    print('dasdsadsadsad',answer)
    for i in range(cnt):
        if ord(letter) +i + 1 > 122 :
            answer += chr(ord('a')+ num)
            num += 1
        else:
            answer += chr(ord(letter) +i +1)             
    return answer    
       
def oneletter(letter, skip, index): # 'a'
    answer =''
    num = 0
    while len(answer) != index:
        cnt = 0
        for i in range(index):
            if ord(letter) +i + 1 > 122 :
                answer += chr(ord('a')+ num) 
                num += 1    
            else:
                answer += chr(ord(letter) +i +1) 
        tmp = ''
        num = 0
        print(answer)
        for letter in answer:
            if letter in skip:
                cnt += 1
            else:
                tmp += letter
        answer = tmp
        print(answer)
        print(cnt)
        num = 0
        print(answer)
        for i in range(cnt):
            if ord(letter) +i + 1 > 122 :
                answer += chr(ord('a')+ num)
                num += 1
            else:
                answer += chr(ord(letter) +i +1) 
                # print(answer)
    return answer            
    #     temp = '' 
    #     cnt2 = 0 
    #     # print(answer)    
    #     for letter in answer:
    #         if letter in skip:
    #             temp += letter
    #             cnt2 += 1
    # num = 0 
    # if cnt2 >= 1:
    #     answer = temp
    #     for i in range(cnt2):
    #         if ord(letter) +i + 1 > 122 :
    #             answer += chr(ord('a')+ num)
    #             num += 1
    #         else:
    #             answer += chr(ord(letter) +i +1)     
    #     return answer[-1]    
    # else:
    #     return answer[-1]       
# print(oneletter('a', 'wbqd', 5)) #> 'h')
print(solution('aukks', 'wbqd', 5)) #> 'g')
# print(solution('zzzzzz', 'abcdefghijklmnopqrstuvwxy', 6))
# print(solution('yy', 'cd', 2))

       
    
        
