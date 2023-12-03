

def solution(dirs):
    directions = {"U": [0, 1],
                  "R":[1, 0],
                  "D": [0, -1],
                  "L": [-1, 0]}
    
    dic ={"[0, 0]": 0} #처음 시작 위치
    result =0
    cur_x = cur_y = 0
    for i in range(len(dirs)):
        next_position = directions[dirs[i]] 
        cur_x += next_position[0]
        cur_y += next_position[1]

        print ( cur_x, cur_y, dirs[i])
        if cur_x >5:
            cur_x =5
        elif cur_x < -5:
            cur_x= -5
        if cur_y >5:
            cur_y =5
        elif cur_y < -5:
            cur_y= -5 
            
        if str([cur_x, cur_y]) in dic.keys():
            if dirs[i] in dic[str([cur_x, cur_y])]:
                continue
            else:
                dic[str([cur_x, cur_y])].append(dirs[i])
                result +=1
        else:
            dic[str([cur_x, cur_y])] = [dirs[i]]
            result +=1
    print(dic)
    return result

print(solution("ULURRDLLU"))
print(solution("LULLLLLLU"))