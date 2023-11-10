def solution(name, yearning, photo):
    dict = {}
    for i in range(len(name)):
        dict[name[i]] = yearning[i]
    #print(dict.items())

    sum_list = []
    for p in photo:
        sum = 0
        for s in p:
            if s in dict:
                sum += dict[s]
        
        sum_list.append(sum)
    
    print(sum_list)
    return sum_list


solution(["may", "kein", "kain", "radi"],	[5, 10, 1, 3],	[["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]])
solution(["kali", "mari", "don"],	[11, 1, 55],	[["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])