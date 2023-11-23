#1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
#2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
#3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
#  3.1 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.


from collections import deque


def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append([i, priorities[i]])
    
    result_list = []

    while queue:
         q = queue.popleft()
         if len(result_list) == len(priorities):
              break
         
         if max(priorities) == q[1]:
              result_list.append(q[0])
              priorities[priorities.index(q[1])] = -1
         else:
              queue.append(q) 
   
    print(result_list)
    return result_list.index(location)+1


# 다른 사람 풀이
def solution2(priorities, location):

    queue = []
    answer = 0
    for i in range(len(priorities)):
        #print("외부  ", i)
        for i in range(len(priorities)):
            #print("내부       ", i)
            if max(priorities) == priorities[i]:
                queue.append(i)
                priorities[i] = 0
            
            if len(queue) == len(priorities):
                break
        if len(queue) == len(priorities):
                break    

    #print(queue)  
    
    return queue.index(location)+1

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1],	0))