def init(temp, want):
    for i in want:
        temp[i] = 0
    return temp

def check(temp, want, number):
    for i in range(len(want)):
        if temp[want[i]] !=number[i]:
            return 0
            
    return 1

def solution(want, number, discount):
    want_number = {}

    for i, j in zip(want, number):
        want_number[i] = j

    #print(want_number.items())
    count = 0
    day = 0
    temp ={}
    find = False
    while len(discount) - day >= 10:
        print("Day : ",day)
        temp = init(temp, want)
        
        for num in discount[day:day+10]:
            if num in temp:
                temp[num] += 1
        
        if check(temp, want, number):
            count +=1
            
        day +=1


    return count
    


print(solution(["banana", "apple", "rice", "pork", "pot"],	[3, 2, 2, 2, 1],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]))

print(solution(["apple"],	[10],	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]))

print(solution(["banana", "apple", "rice", "pork"],	[3, 3, 2, 2],	["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "banana", "banana", "apple", "banana"]))