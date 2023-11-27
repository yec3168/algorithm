def solution(operations):
    stack = []
    for i in operations:
        i = i.split(" ")
        if i[0] == "I":
            stack.append(int(i[1]))
            stack.sort()
            print(stack)
        else:
            if len(stack) == 0:
                continue
            if i[1] == "1":
                stack.pop(-1)
            else:
                stack.pop(0)

    stack.sort()
    if len(stack) == 0:
        return [0,0]
    else:
        return[stack[-1], stack[0]]


print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))