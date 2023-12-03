def reverse_direction(d):
    if d == "L":
        return "R"
    elif d =="R":
        return "L"
    elif d =="U":
        return "D"
    elif d == "D":
        return "U"

def solution(dirs):
    directions = {"U": [0, 1],
                  "R":[1, 0],
                  "D": [0, -1],
                  "L": [-1, 0]}
    
    dic ={"[0, 0]": []} #처음 시작 위치
    result =0
    cur_x = cur_y = 0

    for i in range(len(dirs)):
        if dirs[i] not in dic[str([cur_x, cur_y])]:
            dic[str([cur_x, cur_y])].append(dirs[i])

        next_position = directions[dirs[i]] 
        cur_x += next_position[0]
        cur_y += next_position[1]
        
        if cur_x >5:
            cur_x =5
        elif cur_x < -5:
            cur_x= -5
        if cur_y >5:
            cur_y =5
        elif cur_y < -5:
            cur_y= -5 
        reverse_d = reverse_direction(dirs[i])

        if str([cur_x, cur_y]) in dic.keys():
            if reverse_d in dic[str([cur_x, cur_y])]:
                continue
            else:
                dic[str([cur_x, cur_y])].append((reverse_d))
                result +=1
        else:
            dic[str([cur_x, cur_y])] = [(reverse_d)]
            result +=1
      
    return result


print(solution("ULURRDLLU"))
print(solution("RRRRRLLLLL"))
print(solution("UDLRDURL"))
print(solution("LRLRLRLRLRL"))