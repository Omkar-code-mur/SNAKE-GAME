from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
screen = Screen()
screen.setup(width=600, height=600)


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.controls()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_seg(position)

    def add_seg(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.pencolor("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_seg(self.segments[-1].position())

    def mov_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def mov_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def mov_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def mov_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            x_pos = self.segments[seg_num-1].xcor()
            y_pos = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(x_pos, y_pos)
        self.segments[0].forward(MOVE_DISTANCE)

    def controls(self):
        screen.listen()
        screen.onkey(fun=self.mov_up, key="Up")
        screen.onkey(fun=self.mov_down, key="Down")
        screen.onkey(fun=self.mov_right, key="Right")
        screen.onkey(fun=self.mov_left, key="Left")
