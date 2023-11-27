from itertools import permutations

def solution(k, dungeons):
    permutations_list =  list(permutations(dungeons))
    print(permutations_list)

    result = 0
    for i in range(len(permutations_list)):
        count = 0
        one = k
        for j in permutations_list[i]:
            if one < j[0]:
                break
            else:
                one -=j[1]
                count +=1
        
        result = max(result, count)

    return result




print(solution(80,	[[80,20],[50,40],[30,10]]))