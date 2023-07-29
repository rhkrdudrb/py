# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import deque, defaultdict
import time
import math
def solution(fees, records):
    #recodes 는 시간 기준 오름차순
    #입차와 출차의 누적추자시간
    #초과한 시간이 단위시간으로 나누어 안떨어지면 올림
    #기본시간이하면  ->기본요금
    #기본시간 초과면 -> [누적추자시간 - 기본시간 / 단위시간] * 주차요금
    #입차되고 출차 내용이 없다 -> 23:59에 출차
    #차량번호가 작은 자동차 부터 return
    base_time, base_fee, time_unit, fee_unit = fees
    # 60, 1500, 10, 100
    # time: 135
    # 1500 + (130 - 60) / 10 * 100 
    # 1500 + math.ceil((135 - 60) / 10) * 100 # 7.5 -> 8
    # math.ceil(7) -> 7
    def fee(time):
        if time <= base_time:
            return base_fee
        return base_fee + math.ceil((time - base_time) / time_unit) * fee_unit
# 334
# [180, 5000, 10, 600]
# 5000 + 16 * 600 = 

    num2intime = {}
    num2total = defaultdict(int) # 차량 번호별로 주차한 시간
    for word in records:
        time, num, in_out = word.split() # "13:00", "1234", "OUT"
        if in_out == 'IN':
            num2intime[num] = time
        else:
            num2total[num] += in_out_time(time) - in_out_time(num2intime[num]) # "11:00"    , num in num2intime # bool
            del num2intime[num]
    for num, intime in num2intime.items():
        num2total[num] += in_out_time('23:59') - in_out_time(intime)
    print(num2total)
    print("fee", fee(334))
    answer = []
    for num in sorted(num2total.keys()):
        time = num2total[num]
        answer.append(fee(time))
    return answer


    # {"1234": 120, "5678": 230}

    # IN 1234, 11시 >> 1234 -> 11시 저장 num2intime : {"1234": "11:00", "5678": "11:00"}
    # IN 5678, 11시 >> 1234 -> 11시 저장
    # OUT 1234, 1시 >> 1234 -> 2시간 저장
    # IN 1234, 3시 >> 1234 -> 3시 저장
    # OUT 1234, 4시 >> 1234 -> 1시간 저장 + 1시간 저장 추가 >> 1234 -> 2시간


    # while in_car:
    #     in_time,in_num,in_out = in_car.popleft()
    #     check = True
    #     for i,word in enumerate(out_car):
    #         if word[1] == in_num:
    #             answer.append((in_num,in_out_time(word[0]) - in_out_time(in_time)))
    #             del out_car[i]
    #             check = False
    #             break
    #     if check:
    #         last_car.append([in_time,in_num])
            
    # for i,word in enumerate(last_car):
    #     answer.append((last_car[i][1],in_out_time('23:59') - in_out_time(last_car[i][0])))


    # for문을 다 돌고나면 차량별로 요금 계산


    # answer.sort()
    # last_info = {}
    # for i,word in enumerate(answer):
    #     if word[0] in last_info:
    #         last_info[word[0]] = (last_info[word[0]] + word[1])
    #         continue
    #     last_info[word[0]] = word[1]
        
    # for i in last_info:
    #     if last_info[i] > fees[0]:
    #         if (last_info[i]-fees[0])%fees[2] !=0:
    #             result.append(fees[1] + (math.ceil((last_info[i]-fees[0])/fees[2]) * fees[-1]))
    #         else:
    #             result.append(fees[1] + ((last_info[i]-fees[0])/fees[2] * fees[-1]))
    #     else:
    #         result.append(fees[1])
    # return result
def in_out_time(time):
    all_time = 0
    all_time += int(time[:2])*60
    all_time += int(time[3:5])
    return all_time
print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))