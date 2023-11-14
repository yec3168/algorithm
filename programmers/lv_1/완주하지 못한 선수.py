import collections as col

# list로 하게되면 시간 초과
# 딕셔너리의 시간 복잡도는 O(1)이기때문에 딕셔너리로 풀어야함
def solution(participant, completion):
    dic = col.Counter(participant) # dictionary
    for i in completion:
        if i in dic and dic[i] != 0:
            dic[i] -=1
    
    for i, j in dic.items():
        if j == 1:
            return i
 

print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"],	["josipa", "filipa", "marina", "nikola"]))