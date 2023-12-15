import sys

n = int(input())

have_numbers = list(map(int, sys.stdin.readline().split()))

m = int(input())

check_numbers = list(map(int, sys.stdin.readline().split()))

have_numbers.sort()

 
# 이분탐색?
def list_sol2():
    global check_numbers, have_numbers
    result = []
    
    #print(start, end)
    for i in range(len(check_numbers)):
        result.append(0)

    
    for check in range(len(check_numbers)):
       start, end = 0, len(have_numbers)-1
       while start <=end:
            mid = (start + end) // 2 # 중간 값
            if have_numbers[mid] == check_numbers[check]:
                result[check] = 1
                break
            elif have_numbers[mid] > check_numbers[check]:
                end = mid -1
            else:
                start = mid +1

    return result

# 시간초과
def list_sol1():
    global check_numbers, have_numbers
    result = []
    for check in check_numbers:
        find = False
        for have in have_numbers:
            if check == have:
                result.append(1)
                find = True
                break
            
        if find ==False:
            result.append(0)

# 위치가 랜덤
def set_sol():
    result = []
    for check in check_numbers:
        if check in have_numbers:
            result.append(1)
        else:
            result.append(0)
    
    print(result)


result = list_sol2()

for i in result:
    print(i , end=" ")
