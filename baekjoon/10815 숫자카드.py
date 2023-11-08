import sys

n = int(input())

have_numbers = set(map(int, sys.stdin.readline().split()))

m = int(input())

check_numbers = set(map(int, sys.stdin.readline().split()))

print(have_numbers, check_numbers)


def list_sol1():
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

set_sol()
