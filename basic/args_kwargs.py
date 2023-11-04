# args는 파라미터들을 tuple롤 만들어주는 것
# 파라미터들을 여러개 추가하는 것이 아닌 args 하나로 다가능


# 포인터 형식으로 받아오면 args는 list가 됨.
def add(*args):
    sum = 0
    for i in args:
        sum = sum +i
    return sum


def add2(*args):
    sum = 0
    lists = list(args)

    lists[0] = 100

    for i  in lists:
        sum = sum + i
    return sum


print(add(1, 2, 3, 4))

print(add2(10, 20, 30))



# **kwargs는 dictionary 형식


def multiple(**kwargs):
    print(kwargs['name'] + " "+ kwargs['phone'] + " " + kwargs['email'])

    for key, value in kwargs.items():
        print(key +" "+ value)

# name, phon, email은 key
# 나머지는 value
multiple(name = "hi", phone ="10101", email ="naver")