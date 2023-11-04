# 0 과 1로 이루어진 문자열 x
# x의 모든 0을 제거
# 문자열 x의 길이를 C라고 하면 x를 "c를 2진법을 표현한 문자열로 바꿈"

"""
"0111010"는 = "1111"로 바뀜

"1111"의 길이 c = 4 4를 2진법으로 바꾼다면 "100" 
"""


#{:b} 2진법으로 표기

# 결과 [이진 변환 횟수, 제거된 0의 개수]

def solution(s):
    count_1= 0 # 2진 변환 횟수
    count_2 =0 # 2진변환시 제거된 0
    while len(s) != 1:
        count_1 += 1
        str =[]
        for i in s:
            if i == "1":
                str.append(1)
            else:
                count_2 +=1
        
        l = len(str)
        s = format(l, 'b')
    
    return [count_1, count_2]


print(solution("110010101001"))