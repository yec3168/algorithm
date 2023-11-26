#자카드 유사법
# 집합 A, B사이에 자카드 유사도 J(A, B)는 교집합 크기를 합집합 크기로 나눔
# 교집합 / 합집합
# 둘다 공집합일 경우 1

# 이 다중집합의 교집합 A ∩ B는 원소 "1"을 min(3, 5)인 3개, 합집합 A ∪ B는 원소 "1"을 max(3, 5)인 5개 가지게 된다

def slice_str(str):
    result = []
    for i in range(0, len(str)-1):
        s = str[i:i+2]
        if s.isalpha():
            result.append(s)
    return result

def solution(str1, str2):
    str1 = slice_str(str.upper(str1))
    str2 = slice_str(str.upper(str2))

    intersection1 = set(str1).intersection(str2) 
    union1 = set(str1).union(str2)

    sum_intersection = sum_union = 0
    for i in intersection1:
        sum_intersection += min(str1.count(i), str2.count(i))
    for i in union1:
        sum_union += max(str1.count(i), str2.count(i))

    if sum_intersection == 0 and sum_union == 0:
        return 1*65536
    
    return int( (sum_intersection/sum_union)*65536)
        

#print(solution("FRANCE",	"french"))
print(solution("aa1+aa2", "AAAA12"))