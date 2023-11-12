#
from collections import deque
dict = {
    "{" : "}",
    "(" : ")",
    "[" : "]"
}
def check(queue):
    result = 1
    temp_queue = list(queue)
    
    stack = []
    #['(', ')', '[', '{', '}', ']']
    for i in temp_queue:
        if not stack: # stack이 비어있으면
            if i in dict.keys():
                stack.append(i)
                continue
            else:
                result =0
                break
        # stack에 마지막 문자 ex) "{" 가 dict에 있고 그 value = }가 i와 같으면 pop 
        if dict[stack[-1]] == i:
            stack.pop()
        elif i in dict.keys():
            stack.append(i)
        
    if len(stack) !=0 :
        result =0

    return result

def solution(s):
    if len(s) % 2 != 0:
        return 0
    
    queue = deque(s)
    result = 0
    for n in range(len(s)):
        result +=check(queue)
        queue.append(queue.popleft())
        
    
    return result

print(solution("[](){}"))

print(solution("}]()[{"))

print(solution("[)(]"))