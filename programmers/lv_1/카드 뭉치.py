import itertools

def solution(cards1, cards2, goal):
    
    i = j = result = 0
    while True:
        if result == len(goal):
            break
        if i >= len(cards1):
            i -=1
        if j >= len(cards2):
            j -=1
        #print(cards1[i], cards2[j], "goal  : ", goal[result])
        if cards1[i] == goal[result]:
            i +=1
            result+=1
            continue
        elif cards2[j] == goal[result]:
            j +=1
            result +=1
            continue
        else:
            break

    if result == len(goal):
        return "Yes"
    else:
        return "No" 
        



print(solution(["i", "drink", "water"],	["want", "to"],	["i", "want", "to", "drink", "water"]))
print(solution(["i", "water", "drink"],	["want", "to"],	["i", "want", "to", "drink", "water"]))