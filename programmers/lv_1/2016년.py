day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]

def solution(a, b):
    list_a = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31 ,30 ,31]
    sum =0
    if a == 1:
        print( (b+7)%7 )
        return day[(b+7)%7]
    else:
        for i in range(a-1):
            sum += list_a[i]
        
        result = (sum+b)%7
        print(result)
    return day[result]


print(solution(5, 24))
print(solution(5, 24))
print(solution(1, 1))
