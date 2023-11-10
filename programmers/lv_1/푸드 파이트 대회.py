# food[0] = 물
# food[1:] = 칼로리가 적은 음식의 수

"""
ex)
[1, 3, 4, 6]
1223330333221 
"""

def solution(food):
    result =""
    count = 0
    for i in range(1, len(food)):
        result += str(i)* (food[i] // 2)

    result = result+"0"+result[::-1]
    
    return result

print(solution([1,3,4,6]))