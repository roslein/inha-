from cs1robots import *
import time
load_world('maze4.wld')
hubo = Robot(beepers=1)
hubo.set_trace("blue")
sleep_time = 0.5

def on_forked_road():
    print((hubo.front_is_clear and hubo.right_is_clear) or (hubo.front_is_clear and hubo.left_is_clear) or (hubo.right_is_clear and hubo.left_is_clear))
    
def mark_starting_point_and_move():
    time.sleep(sleep_time)
    hubo.drop_beeper()
    while not hubo.front_is_clear():
        time.sleep(sleep_time)
        hubo.turn_left()
    time.sleep(sleep_time)
    hubo.move()

mark_starting_point_and_move()
while not hubo.on_beeper():
    hubo.move()
    on_forked_road
