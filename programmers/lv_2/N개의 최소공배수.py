def solution(arr):
    i = 1
    while True:
        count = 0
        for num in arr:
            if i % num == 0:
                count +=1
        
        if count == len(arr):
            break;
        else:
            i +=1
    
    return i




print(solution([2,6,8,14]))