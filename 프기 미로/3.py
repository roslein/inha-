from cs1robots import *
import time
load_world('maze4.wld')
hubo = Robot(beepers=99)
hubo.set_trace("blue")
sleep_time = 0.5

def turn_right():
    for i in range(3):
        hubo.turn_left()


def mark_starting_point_and_move():
    time.sleep(sleep_time)
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

def on_two_beeper():
    if hubo.on_beeper():
        hubo.pick_beeper()
        if hubo.on_beeper():
            hubo.drop_beeper()
            return True
        else:
            hubo.drop_beeper()
            return False
    else:
        return False


    
def on_forked_road():
    if hubo.front_is_clear() and hubo.right_is_clear():
        return True
    elif hubo.front_is_clear() and hubo.left_is_clear():
        return True
    elif hubo.right_is_clear() and hubo.left_is_clear():
        return True
    else:
        return False

def on_one_beeper():
    if hubo.on_beeper():
        hubo.pick_beeper()
        if hubo.on_beeper():
            hubo.drop_beeper()
            return False
        else:
            return True
    else:
        return False

    
        


mark_starting_point_and_move()
while not on_one_beeper():
    if on_two_beeper():
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
            hubo.turn_left()
            hubo.move()
    elif on_forked_road():
         hubo.drop_beeper()
         hubo.drop_beeper()
         follow_left_wall()
    else:
        follow_left_wall()
    
