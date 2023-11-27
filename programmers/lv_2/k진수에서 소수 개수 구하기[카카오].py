def solution(n, k):
    temp = ""
    while n >0:
        temp += str(n%k)
        n = n//k
    # k진수로 만들기
    temp = temp[::-1]
    temp = temp.split("0")
    temp = [i for i in temp if i]


    result = 0
    for i in temp:
        int_i = int(i)
        if int_i == 1:
            continue
        elif int_i <=3:
            result +=1
            continue
        else:
            find = True
            for j in range(2, int(int_i ** 0.5)+1):
                if int_i % j ==0:
                    find = False
                    break
        
        if  find == True:
            result +=1

    return result
        


print(solution(437674,	3))
print(solution(110011,	10))