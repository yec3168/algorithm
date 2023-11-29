def init_dic():
    dic ={}
    count =0
    for i in range(16):
        if i>=10:
            dic[str(i)] = chr(65+count)
            count +=1
        else:
            dic[str(i)] = str(i)
    return dic

def solution(n, t, m, p):
    total = m*t
    temp=""
    dic = init_dic()
 
    # ex) 8이면
    # 0 1 10 11 100 101 110 111 1000
    for i in range(total+1):
        a =""
        if i == 0:
            a += dic[str(i)]
        else:
            while i >0:
                a +=dic[str(i%n)]
                i = i // n
        a = a[::-1]
        temp += a
    
    result =""
    for i in range(p-1, (m*t), m):
        result += temp[i]
    
    return result

print(solution(2,	4,	2,	1))

