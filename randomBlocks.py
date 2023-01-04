import random
from turtle import Turtle


class Blocks:
    def __init__(self):
        self.colors = ["red", "yellow", "green", "orange", "blue", "purple"]
        self.block_list = []

    def make_a_block(self):
        Block_1 = Turtle()
        Block_1.shape("square")
        Block_1.penup()
        Block_1.goto(500, random.randint(-375, 375))
        Block_1.color(random.choice(self.colors))
        Block_1.shapesize(stretch_wid=1, stretch_len=random.randint(1, 6))
        self.block_list.append(Block_1)

    def move_blocks(self):
        for element in self.block_list:
            element.backward(10)
