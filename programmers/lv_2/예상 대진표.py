def solution(n,a,b):
    count =1
    while True:
        if a % 2 == 0:
            a = a//2
        else:
            a = (a+1)//2 
        if b % 2 == 0:
            b = b//2
        else:
            b = (b+1)//2
        # a == 4 b ==5인경우는 끝에서 만남
        if a==b:
            break
        count +=1
       
        
    return count
        

print(solution(8, 4, 5))