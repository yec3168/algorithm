def binary_list(n, array):
    result_list = []
    for i in array:
        temp = format(i, 'b')
        if len(temp) < n:
            temp = '0'*(n-len(temp)) + temp
        result_list.append(temp)
    
    return result_list

def solution(n, arr1, arr2):
    result_list = []

    arr1_binary=binary_list(n, arr1)
    arr2_binary=binary_list(n, arr2)
    
    for i in range(n):
        temp =""
        for count in range(n):
            print(arr1_binary[i][count],  arr2_binary[i][count])
            if arr1_binary[i][count] == arr2_binary[i][count]:
                if arr1_binary[i][count] == '1':
                    temp += "#"
                else:
                    temp += " "
            else:
                temp += "#"
        
        result_list.append(temp)
    return result_list

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))

print(solution(6	,[46, 33, 33 ,22, 31, 50]	,[27 ,56, 19, 14, 14, 10]))