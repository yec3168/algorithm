def solution(array, commands):

    result_list = []

    for command in commands:
        temp = array[command[0]-1:command[1]]
        temp.sort()
        result_list.append(temp[command[2]-1])
    print(result_list)


solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])