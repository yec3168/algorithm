n = int(input())

temp = n
def number(cnt, temp):
    global n
    number_list = list(map(int, str(temp)))

    sum = 0
    for i in number_list:
        sum += i

    new_num = int(str(number_list[len(number_list)-1]) + str(sum%10))
    
    if new_num == n:
        print(cnt)
        return 0
    else:
        number(cnt+1, int(new_num))
    
number(1, temp)