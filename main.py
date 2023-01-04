import random
import time
import randomBlocks
from turtle import *
import make_to_move

screen = Screen()
screen.setup(1000, 750)
blocks_list = []
tracer(0)
block = randomBlocks.Blocks()
gameison = True
turt = make_to_move.make_player().make_turtle()
while gameison:
    randon_choice = random.randint(1, 6)
    if randon_choice == 1:
        block.make_a_block()

    block.move_blocks()
    update()
    time.sleep(0.5)

screen.exitonclick()
