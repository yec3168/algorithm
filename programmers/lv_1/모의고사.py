#1번  -> 1234512345
#2번  -> 212324252123
#3번  -> 33112244553311224455


def solution(answers):
    result_list =[]
    first_student = [1, 2, 3, 4, 5]
    second_student = [2, 1, 2, 3, 2, 4, 2, 5]
    third_student = [3, 3, 1, 1, 2, 2, 4, 4 ,5, 5]
    one = two = three = 0

    for answer in range(len(answers)):
        if answers[answer] == first_student[(answer+5)%5]:
            one +=1
        if answers[answer] == second_student[(answer+8)%8]:
            two +=1
        if answers[answer] == third_student[(answer+10)%10]:
            three +=1

    answer_dict = { "1" : one,
                    "2" : two,
                    "3" : three }
    
    answer_dict = sorted(answer_dict.items(), key = lambda x : (x[1]), reverse=True)
    if answer_dict[0][1] == 0:
        return result_list
    
    temp =[]
    temp.append(list(answer_dict[0]))
    for i in range(1,len(answer_dict)):
        if temp[i-1][1] == answer_dict[i][1]:
            temp.append(list(answer_dict[i]))
        else:
            break
        
    for i in temp:
        result_list.append(int(i[0]))   
    return result_list


print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))