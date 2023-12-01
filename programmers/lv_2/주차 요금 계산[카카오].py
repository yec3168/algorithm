# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59에 출차된 것으로 간주합니다.

#누적 주차 시간이 기본 시간이하라면, 기본 요금을 청구합니다.
#누적 주차 시간이 기본 시간을 초과하면, 기본 요금에 더해서, 초과한 시간에 대해서 단위 시간 마다 단위 요금을 청구합니다.
#초과한 시간이 단위 시간으로 나누어 떨어지지 않으면, 올림합니다.

import datetime
import math
def calculate(fees, fee_records):
    fee_records = sorted(fee_records , key=lambda x : x[0])
    result = []
    for record in fee_records:
        if fees[0] > record[1]:
            result.append(fees[1])
        else:
            result.append(fees[1]+( math.ceil((record[1]-fees[0])/fees[2]) * fees[3]))
    return result


def solution(fees, records):
    fee_records = [] # [차량번호 , 시간]
    stack = []  # [시간 , 차량번호]
    for i in records:
        split_i = i.split(" ")
        
        if split_i[2] =='IN':
            stack.append([split_i[0], split_i[1]])
        else:
            temp =[]
            # 제거
            for s in stack:
                if split_i[1] == s[1]:
                    temp = s
                    stack.remove(s)
                    break
            split_i_time = datetime.datetime.strptime(split_i[0], "%H:%M")
            temp_time = datetime.datetime.strptime(temp[0], "%H:%M")
            temp_time = (split_i_time - temp_time).seconds
            
            find = False
            for f in range(len(fee_records)):
                if temp[1] ==  fee_records[f][0]:
                    fee_records[f][1] += temp_time//60
                    find = True
                    
                    break
            if find == False:
                fee_records.append([temp[1], temp_time//60])
    if len(stack) != 0:
        for i in stack:
            split_i_time = datetime.datetime.strptime(i[0], "%H:%M")
            temp = datetime.datetime.strptime("23:59", "%H:%M")
            temp_time = (temp - split_i_time).seconds
            find = False
            for f in range(len(fee_records)):
                if i[1] ==  fee_records[f][0]:
                    fee_records[f][1] += temp_time//60
                   
                    find = True
                    break
            if find == False:
                fee_records.append([i[1], temp_time//60])
    
    return calculate(fees, fee_records)






print(solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))