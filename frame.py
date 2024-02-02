import turtle
class FrameTurtle(turtle.Turtle):

    screen: object
    t: object

    def __init__(self, screen = None):
        '''
        Method:    This is the object draw the Frame
        Parameter: self
        Return   : None
        '''
        self.screen = screen
        self.t = turtle.Turtle()
        self.draw_frame(-420, 420, 450, 500,"black")
        self.draw_frame(70, 420, 230, 500, "blue")
        self.draw_frame(-420, -140, 720, 120, "black")
        

    def draw_frame(self, x, y, width, height, color):
        '''
        Method:    Create a turtle to draw the stage
        Parameter: self
        Return   : None
        '''
        self.t.speed(10)
        self.t.pensize(7)
        self.t.color(color)
        self.t.penup()
        self.t.goto(x,y)
        self.t.setheading(90)
        self.t.right(90)
        self.t.pendown()
        for i in range(2):
            self.t.forward(width)
            self.t.right(90)
            self.t.forward(height)
            self.t.right(90)
    
    def display_error(self):
        self.screen.addshape("./Resources/Resources/file_error.gif")
        self.t.shape("./Resources/Resources/file_error.gif")
        time.sleep(3)
        exit()