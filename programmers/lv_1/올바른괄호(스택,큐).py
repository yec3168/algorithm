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



# def solution(s):
#     queue =[]
#     result = False
#     for i in s:
#         queue.append(i)

#     # 첫 번째가 ")"이거나 큐의 수가 홀수면 False
#     if queue[0]== ")" or len(queue) % 2 != 0 or len(queue) == 0:
#         return result

#     count =[0, 0]

#     for i in queue:
#         if i == "(":
#             count[0] = count[0] + 1
#         else:
#             count[1] = count[1] + 1
        
#     if count[0] == count[1]:
#         result = True
    
#     return result



str ="()()"
print(solution(str))