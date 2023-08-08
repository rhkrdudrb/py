# https://school.programmers.co.kr/learn/courses/30/lessons/67257
from itertools import *
def solution(expression):
    toks = parse(expression)
    print(toks)
    orders = set()
    for word in toks:
      print(word)
      if word == '*':
        orders.add(word)
      elif word == '-':
        orders.add(word)
      elif word == '+':
        orders.add(word)   
    orders = list(permutations(list(orders), len(orders)))
    print(orders)
    max_list = []
    for order in orders:
      max_list.append(abs(evaluation(toks,order)))
    print(max_list)
    return max(max_list)
# "100-200*300-500+20" >> [100, '-', 200, '*', 300, '-', 500, '+', 20]
# toks: [100, '-', 200, '*', 300, '-', 500, '+', 20], orders: ['*', '+', '-']
# 100 - (200 * 300) - 500 + 20 
# 100 - 60000 - (500 + 20) toks : [100, '-', 60000, '-', 500, '+', 20]
# 100 - 60000 - 520
# -59900 - 520
# -60420
def evaluation(toks, orders):
    idx = 0
    while len(toks) != 1:
        i = 0
        while i < len(toks):
            tok = toks[i]
            if tok == orders[idx]:
                tok_result = eval(toks[i-1], tok, toks[i+1])
                # toks = toks[:i-1] + [toks[i-1], toks[i], toks[i+1]] + toks[i+2:]
                toks = toks[:i-1] + [tok_result] + toks[i+2:] #[]
                print(toks)
                if orders[idx] in toks:
                  continue
                idx +=1
            i += 1
    return toks[0]
# idx 넘어가는 방법 고민
# orders에 순서 다양하게 넣는 방법 고민
# eval(200, '*', 300) >> 60000
# eval(10, '-', 20) >> -10
# evall(500, '+', 20) >> 520
def eval(num1, op, num2):
    if op == '*':
        return num1 * num2
    elif op == '-':
        return num1 - num2
    else: # op == '+'
        return num1 + num2
# '100-200' >> [100, '-', 200]
def parse(expression):
    toks = []
    idx = 0
    while idx < len(expression):
        num = 0
        while idx < len(expression) and expression[idx].isdigit(): # 1
            num *= 10 # 0 10
            num += int(expression[idx]) # 1 10
            idx += 1
        if num !=0:
            toks.append(num) # [0,0,0]
        else: # num == 0
            toks.append(expression[idx]) # ['1','0']
            idx += 1
    return toks
# "3+0" >> [3, '+', 0]
#num op num op num op .... num
# s = '100'
# idx = 0
# num = 0
# while idx < len(s) and s[idx].isdigit():
#     num *= 10 # 100
#     num += int(s[idx])
#     idx += 1 # 3
# return num

print(solution("100-200*300-500+20")) #60420
print(solution("50*6-3*2")) #300
# '*', '+', '-'
# nums = [100, 200, 300, 500, 20]
# ops = [-, *, -, +]

-----------------------------------------------------------------------

def solution(expression):
    toks = parse(expression)
    return evaluation(toks, ['*', '+', '-'])   

# "100-200*300-500+20" >> [100, '-', 200, '*', 300, '-', 500, '+', 20]
# toks: [100, '-', 200, '*', 300, '-', 500, '+', 20], orders: ['*', '+', '-']
# 100 - (200 * 300) - 500 + 20 
# 100 - 60000 - (500 + 20) toks : [100, '-', 60000, '-', 500, '+', 20]
# 100 - 60000 - 520
# -59900 - 520
# -60420

def evaluation(toks, orders):
    idx = 0
    while len(toks) != 1:
        i = 0
        while i < len(toks):
            tok = toks[i]
            if tok == orders[idx]:
                tok_result = eval(toks[i-1], tok, toks[i+1])
                # toks = toks[:i-1] + [toks[i-1], toks[i], toks[i+1]] + toks[i+2:]
                toks = toks[:i-1] + [tok_result] + toks[i+2:] #[]
                if orders[idx] in toks:
                    
                
            i += 1
    return toks[0]

# idx 넘어가는 방법 고민
# orders에 순서 다양하게 넣는 방법 고민


# eval(200, '*', 300) >> 60000
# eval(10, '-', 20) >> -10
# evall(500, '+', 20) >> 520
def eval(num1, op, num2):
    if op == '*':
        return num1 * num2
    elif op == '-':
        return num1 - num2
    else: # op == '+'
        return num1 + num2

# '100-200' >> [100, '-', 200]
def parse(expression):
    toks = []
    idx = 0
    while idx < len(expression):
        num = 0
        while idx < len(expression) and expression[idx].isdigit(): # 1
            num *= 10 # 0 10
            num += int(expression[idx]) # 1 10
            idx += 1
        if num !=0:
            toks.append(num) # [0,0,0]
        else: # num == 0
            toks.append(expression[idx]) # ['1','0']
    return toks
# "3+0" >> [3, '+', 0]
#num op num op num op .... num
# s = '100'
# idx = 0
# num = 0
# while idx < len(s) and s[idx].isdigit():
#     num *= 10 # 100
#     num += int(s[idx])
#     idx += 1 # 3
# return num

print(solution("100-200*300-500+20")) #60420
print(solution("50*6-3*2")) #300
# '*', '+', '-'
nums = [100, 200, 300, 500, 20]
ops = [-, *, -, +]

