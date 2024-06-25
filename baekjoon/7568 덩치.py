import sys
input = sys.stdin.readline

def solution(users):
    result = ""
    for user in users:
        ranking = 1
        #print(user)
        for j in range(len(users)):
            #print("users : " ,users[j][0], users[j][1])
            if(user[0] < users[j][0] and user[1] < users[j][1]):
                #print("통과")
                ranking +=1
        
        result = result + str(ranking) + " "
    
    print(result)

n = int(input())
users = []

for _ in range(n):
    kg, tall = input().split()
    users.append([int(kg), int(tall)])
    
solution(users)