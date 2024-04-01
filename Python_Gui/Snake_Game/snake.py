from turtle import Screen, Turtle

starting_positions = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        #add a new segment to the snake
        self.add_segment(self.segments[-1].position())
        #print(self.segments[-1].position())

    def create_snake(self):
        #the new segment gets created and segments ain't empty no more
        for position in starting_positions:
            self.add_segment(position)
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1): 
#it tells it to count down backwards and since list starts from 0, there will be a -1 for the segment for correct values
            new_x = self.segments[seg_num - 1].xcor() 
#it gets the x co-ordinate of the segment in front of it
            new_y = self.segments[seg_num - 1].ycor()
#it gets the y co-ordinate of the preceding segment
            self.segments[seg_num].goto(new_x, new_y)
#tells it to go to the x and y segment
        self.head.forward(MOVE_DISTANCE)
#tells the first segment to move forward

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
