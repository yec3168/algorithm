# 봉지는 3kg, 5kg가 있음.
#  최대한 적은 봉지를 들고 가려고 함.
# ex( 18kg -> 5kg * 3 , 3kg *1)




def solution(n):
    
    result = 0

    while n  > 0:
      if n % 5  == 0:
        result += n //5
        n = n % 5
      else:
         n -= 3
         result +=1

    if n != 0:
        return -1
    return result
        
        
    

n = int(input())

print(solution(n))