#1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
#2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
#3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
#4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
#5. 단계 2로 돌아간다.
def solution(msg):
    dic = {}
    count = 27# 알파벳 대문자 개수 
    for i in range(1, count):
        dic[chr(64+i)] = i


    result = []
    cur = 0
    while True:
        one =""
        for i in range(len(msg)):
            one = msg[cur:len(msg)-i]
            if one in dic:
                result.append(dic[one])
                break
        # 종료
        if cur+len(one) >= len(msg):
            break
        elif cur+len(one) < len(msg)-1:
            temp = one+msg[cur+len(one)]
            dic[temp] = count
            count +=1
        else:
            temp = one
            dic[temp] = count
            count+=1
        
        cur +=len(one)

    return result

print(solution("KAKAO"))
print(solution("TOBEORNOTTOBEORTOBEORNOT"))