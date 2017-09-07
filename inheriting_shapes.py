import Tkinter # built-in Python graphics library
import random

game_objects = []

class Shape:
    def __init__(self, x, y):
        '''Create a new circle at the given x,y point with a random speed, color, and size.'''
        
        self.x = x
        self.y = y

        self.x_speed = random.randint(-5,5)
        self.y_speed = random.randint(-5,5)

        while self.x_speed == 0 or self.y_speed == 0:
            self.x_speed = random.randint(-5,5)
            self.y_speed = random.randint(-5,5)

        # this creates a random hex string between #000000 and #ffffff
        # we draw it with an outline, so we'll be able to see it on a white background regardless
        self.color = '#{0:0>6x}'.format(random.randint(00,16**6))
        self.size_1 = random.randint(5,40)
        self.size_2 = random.randint(5,40)

    def update(self):
        '''Update current location by speed.'''

        self.x += self.x_speed
        self.y += self.y_speed

class Circle(Shape):
    def draw(self, canvas):
        '''Draw self on the canvas.'''

        canvas.create_oval(self.x-self.size_1, self.y-self.size_1, self.x + self.size_1, self.y + self.size_1, fill=self.color, outline="")

class Rect(Shape):
    def draw(self, canvas):
        '''Draw self on the canvas.'''
        
        canvas.create_rectangle(self.x-self.size_1, self.y-self.size_2, self.x + self.size_1, self.y + self.size_2, fill=self.color, outline="")

class Triangle(Shape):
    def draw(self, canvas):
        '''Draw self on the canvas.'''
        canvas.create_polygon(self.x, self.y-self.size_2, self.x-self.size_1, self.y+self.size_2, self.x+self.size_1, self.y+self.size_2, fill=self.color, outline="")

def addShape(event):
    '''Add new shapes where the user clicked.'''

    global game_objects
    constructor = random.choice([Circle, Rect, Triangle])
    game_objects.append(constructor(event.x, event.y))

def reset(event):
    '''Clear all game objects.'''

    global game_objects
    game_objects = []

def draw(canvas):
    '''Clear the canvas, have all game objects update and redraw, then set up the next draw.'''

    canvas.delete(Tkinter.ALL)

    global game_objects
    for game_object in game_objects:
        game_object.update()
        game_object.draw(canvas)

    delay = 33 # milliseconds, so about 30 frames per second
    canvas.after(delay, draw, canvas) # call this draw function with the canvas argument again after the delay

# this is a standard Python thing: definitions go above, and any code that will actually
# run should go into the __main__ section. This way, if someone imports the file because
# they want to use the functions or classes you've defined, it won't start running your game
# automatically
if __name__ == '__main__':

    # create the graphics root and a 400x400 canvas
    root = Tkinter.Tk()
    canvas = Tkinter.Canvas(root, width=1600, height=900, background="black")
    canvas.pack()
    
    # if the user presses a key or the mouse, call our handlers
    root.bind('<Key-r>', reset)
    root.bind('<Button-1>', addShape)

    # start the draw loop
    draw(canvas)

    root.mainloop() # keep the window open

