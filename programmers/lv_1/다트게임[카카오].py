#Single(S), Double(D), Triple(T) (점수1 , 점수2 , 점수3 ) 1제곱, 2제곱, 3제곱
#스타상(*) 점수를 각 2배 , 아차상(#)해당 점수는 마이너스
# 스타상이 처음 나왔을때는 첫번째 스타상 점수만 2배
# 스타상은 중첩이 가능하다. 2^으로 계산
# 스타상 아차상 중첩시 -2배

def solution(dartResult):
    # 리스트 중첩으로 만들기
    s = ""
    temp =[]
    for i in range(len(dartResult)):
        if dartResult[i].isalpha():
            if dartResult[i] == 'S':
                temp.append(pow(int(s), 1))
            elif dartResult[i] =='D':
                temp.append(pow(int(s), 2))
            elif dartResult[i] =='T':
                temp.append(pow(int(s), 3))
            s =""
        else:
            if dartResult[i].isdigit():
                s +=dartResult[i]
            elif dartResult[i] == "*":
                if len(temp) <2:
                    temp[-1] *=2
                else:
                    for i in range(len(temp)-1, len(temp)-3, -1):
                        temp[i] *=2
            else:
                temp[-1] *= -1
            
    return sum(temp)

print(solution('1S*2T*3S'))
