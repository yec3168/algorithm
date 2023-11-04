def solution(s):
    position = 0

    for i in s:
        if i =="(":
            position +=1
        elif i == ")":
            position -=1
        if position < 0:
            return False


    if position == 0:
        return True
    else:
        return False



str ="()()"
print(solution(str))