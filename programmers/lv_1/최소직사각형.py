#최소 직사각형

"""
 60 50
 30 70
 60 30
 80 40

 가로와 세로가 가장 큰 = 80 * 70 다 들어가긴 함

 2번쨰 명함  30 * 70을 가로로 눞혀 70 * 30으로 만들면

 80 * 50 크기의 지갑으로도 가능 

  # 경우의 수
60 50,    50  6
"""


"""
x + y  = z 일떄

y = (z- x) 가 되고, 가로 * 세로 = zx- x^2이 된다.

위로 볼록한 형태가 되며 기울기가 0인 지점 이 최대값이 된다

미분하게 되면 z - 2x

x = z/2  y = z/2 이므로 x가 최대값일때 y가최소값을 가지면 정답
"""
def solution(sizes):

    max_h = max_w = 0
    for i in sizes:
        w, h = i 

        max_w = max(max_w, w, h)

        max_h = max(max_h, min(w, h))

        print(max_w, max_h)



    return max_w * max_h

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

