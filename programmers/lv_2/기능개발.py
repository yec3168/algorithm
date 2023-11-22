#progresses는 먼저 개발되어야할 순서대로 저장

from collections import deque

def solution(progresses, speeds):
    result = []
    queue = deque(progresses)
    count =0

    while queue:
        if queue[0] >= 100:
            temp = []
            for i in range(len(queue)):
                if queue[i] >=100:
                    temp.append(i)
                    count +=1
                else:
                    break
            result.append(count)
            for i in range(count):
                queue.popleft()

            for i in temp[len(temp)::-1]:
                speeds.pop(i)
            count =0

        for i in range(len(queue)):
            queue[i] += speeds[i]  
            

    return result


# solution2 100퍼 넘은 모든 작업들을 첫번째 작업이 끝나면 삭제
def solution(progresses, speeds):
    
    stack =[]
    result = []
    count = 0
    temp = []
    while True:
        if len(progresses) == 0:
            break

        if progresses[0] >= 100:
            result.append(count)
            count = 0

            if len(temp) !=0:
                temp.sort()
                for i in temp[len(temp):: -1]:
                    speeds.pop(i)
                    progresses.pop(i)
                temp = []
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]  
            if progresses[i] >= 100:
                 if i not in temp:
                    count +=1
                    temp.append(i)


    return result

print(solution([93, 30, 55],	[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],	[1, 1, 1, 1, 1, 1]))