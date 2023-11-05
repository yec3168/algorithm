def bunhae_hab(n):
    result = 0
    for i in range(n):
        result = i
        # for j in list(str(i)):
        #     result += int(j)
        
        num_list = list(map(int, list(str(i))))

        result += sum(num_list)
        if result == n:
            return i
    return 0

n = int(input())

print(bunhae_hab(n))