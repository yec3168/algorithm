def solution(strings, n):
    
    strings = sorted(strings, key= lambda x: (x[n], x[0:]))
    return strings

print(solution(["sun", "bed", "car"], 1))