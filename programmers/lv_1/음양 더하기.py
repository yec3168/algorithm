def solution(absolutes, signs):
    result = 0
    for i in range(len(absolutes)):
        if signs[i] == False:
            absolutes[i] = -absolutes[i]
        result = result + absolutes[i]
    return result

print(solution([4,7,12], [True,False,True]))


# 다른 사람 풀이

def sol2(absolutes, signs):
    return sum(absolute if sign else -absolute for absolute, sign in zip(absolutes, signs))

print(sol2([4,7,12], [True,False,True]))