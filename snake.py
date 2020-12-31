from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self._create_snake()
        self.head = self.segments[0]

    def _create_snake(self):
        for snake_position in STARTING_POSITION:
            self.add_segment(snake_position=snake_position)

    def add_segment(self, snake_position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(snake_position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_num in range(len(self.segments ) - 1, 0, -1):
            self.segments[segment_num].goto(self.segments[segment_num - 1].xcor(), self.segments[segment_num - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)