https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import deque
import time
from datetime import datetime
def solution(fees, records):
    answer = []
    records_info = []
    in_car = deque() #
    out_car= deque() #
    last_car = []
    for word in records:
        records_info = word.split()
        if records_info[-1] == 'IN':
            in_car.append(records_info)
        else:
            out_car.append(records_info)
    while in_car:
        in_time,in_num,in_out = in_car.popleft()
        check = True
        for i,word in enumerate(out_car):
            if word[1] == in_num:
                # print(word[1],' ',in_num,'  ',word[0],'  ',in_time)
                answer.append(in_out_time(word[0]) - in_out_time(in_time))
                del out_car[i]
                check = False
                break
        if check:
            last_car.append([in_time,in_num,in_out])
            
    print(last_car)
    print(answer)
    #recodes 는 시간 기준 오름차순
    #입차와 출차의 누적추자시간
    #초과한 시간이 단위시간으로 나누어 안떨어지면 올림
    #기본시간이하면  ->기본요금
    #기본시간 초과면 -> [누적추자시간 - 기본시간 / 단위시간] * 주차요금
    #입차되고 출차 내용이 없다 -> 23:59에 출차
    #차량번호가 작은 자동차 부터 return
    return answer
def in_out_time(time):
    all_time = 0
    all_time += int(time[:2])*60
    all_time += int(time[3:5])
    return all_time
