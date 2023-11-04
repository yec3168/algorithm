def solution(s):
    list = s.split(" ")
    result =""
    for i in range(len(list)):
       list[i]  = list[i].capitalize()
        
    
    return " ".join(list)


print(solution("3people unFollowed me"))



# 다른 사람풀이

def sol2(s):
    return s.title()

print(sol2("3people unFollowed me"))
