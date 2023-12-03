def solution(babbling):
    speaks = ["aya", "ye", "woo", "ma"]
    result = 0
    for i in range(len(babbling)):
        for speak in speaks:
            # 일단 단어가 들어 있으면
            if speak in babbling[i]:
                speak_count = babbling[i].count(speak)
                find = True
                if speak_count >=2:
                    first = babbling[i].find(speak)
                    #print("speak :", speak, "babbling :", babbling[i] , "   ", first)
                    for j in range(1, speak_count):
                        two = babbling[i].find(speak, first+1)
                        #print("two-first", two-first)
                        if two - first == len(speak):
                            find = False
                            continue
                        else:
                            babbling[i] = babbling[i][first+len(speak)-1:]
                            first= two
                if find == True:
                    babbling[i] = babbling[i].replace(speak, "*")
    print(babbling)
    
    a = True
    for i in babbling:
        if len(i) == 0:
            result +=1   
                

    return result

    


print(solution(["aya", "yee", "u", "maa"]))

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))

print(solution(["ayamayaa"]))