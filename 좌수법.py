from cs1robots import *
import time
load_world('maze4.wld')
hubo = Robot(beepers=1)
hubo.set_trace("blue")
sleep_time = 0.5

def turn_right():
    for i in range(3):
        hubo.turn_left()


def mark_starting_point_and_move():
    time.sleep(sleep_time)
    hubo.drop_beeper()
    while not hubo.front_is_clear():
        time.sleep(sleep_time)
        hubo.turn_left()
    time.sleep(sleep_time)
    hubo.move()

def follow_left_wall():
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

mark_starting_point_and_move()

while not hubo.on_beeper():
    follow_left_wall()

