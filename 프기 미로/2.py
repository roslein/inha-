#*******************************
#CS101 Introduction to Programming
#Homework #1
#*********************
#*******************************


from cs1robots import *
import time

#load_world("**")
load_world("maze4.wld") #숙제할때 테스트용으로 주어진맵 -,.-

hubo = Robot(beepers=1 )
#미로안에 들어간 놈. 실제로 맵에 구현할때 x, y, orientation 저장해두세요.
hubo.set_trace("blue")
sleep_time = 0.5

angular_sum = 0
#이 스프링 역할을 해주는 변수가 중요합니다. 이 알고리즘의 핵심임.

def turn_left():
    
    hubo.turn_left() #orientation 변수를 왼쪽으로 꺾는 단순 메소드
    global angular_sum
    angular_sum += 1 # 왼쪽으로 꺾으면 스프링 1증가.

def turn_right():
    for i in range(3):
        hubo.turn_left() #구현할땐 그냥 orientation을 오른쪽으로 꺾으세요. =,.=
    
    global angular_sum
    angular_sum -= 1 # 오른쪽으로 꺾으면 스프링 1감소.
    
    
##### From here, your code should be.
##### ID: ********, Name: *****************, Lab: *

def tryforward(): #직진용 매크로 함수. 성공시 True, 실패시 False 리턴
    if hubo.front_is_clear():
        hubo.move() #앞으로 한칸 전진 메소드입니다. orientation에 따라 x/y 조절하세요.
        return True
    return False

def wf(): #wall following #넵 벽타기
    if angular_sum < 0 and angular_sum > -20: #오른쪽으로 과하게 꺾었으면 왼쪽으로 꺾기 우선 시도
        if hubo.left_is_clear():
            time.sleep(sleep_time)
            hubo.turn_left()
            time.sleep(sleep_time)
            hubo.move()

        elif hubo.front_is_clear():
            time.sleep(sleep_time)
            hubo.move()
        else:
            time.sleep(sleep_time)
            turn_right()
    elif angular_sum > 0 and angular_sum <20: #왼쪽으로 과하게 꺾었으면 오른쪽으로 꺾기 우선 시도
        if hubo.right_is_clear():
            time.sleep(sleep_time)
            turn_right()
            time.sleep(sleep_time)
            hubo.move()
        elif hubo.front_is_clear():
            time.sleep(sleep_time)
            hubo.move()
        else:
            time.sleep(sleep_time)
            turn_left()
    elif angular_sum <-20:
        if hubo.right_is_clear():
            time.sleep(sleep_time)
            turn_right()
            time.sleep(sleep_time)
            hubo.move()
        elif hubo.front_is_clear():
                time.sleep(sleep_time)
                hubo.move()
        else:
                time.sleep(sleep_time)
                turn_left()
    elif angular_sum >= 20:
        if hubo.left_is_clear():
            time.sleep(sleep_time)
            hubo.turn_left()
            time.sleep(sleep_time)
            hubo.move()
        elif hubo.front_is_clear():
            time.sleep(sleep_time)
            hubo.move()
        else:
            time.sleep(sleep_time)
            turn_right()
        
    else: #사실 여기 분기까지 오는 경우가 꺾인횟수가 밸런스인 채로 직진하다 막힌경우.
            turn_left()
            time.sleep(sleep_time)

    

while not hubo.on_beeper(): #출구를 찾을때까지 반복
    if angular_sum != 0 or not tryforward():
        wf()
   #꺾는횟수가 0이면 벽이고 개뿔이고 일단 직진시도해보고 안되면 벽타긔
   #꺾는횟수가 언밸런스면 닥치고 벽타긔
hubo.pick_beeper()
