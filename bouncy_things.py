import Tkinter # built-in Python graphics library
import random
import math

game_objects = []

class Circle:
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
		self.radius = random.randint(2,40)

	def update(self):
		'''Update current location by speed.'''

		self.x += self.x_speed
		self.y += self.y_speed
		
		# bounces the circles off of the edge of the screen
		if self.x >= 400 - self.radius:
			self.x_speed = -abs(self.x_speed)
		if self.x <= 0 + self.radius:
			self.x_speed = (abs(self.x_speed))
		
		if self.y >= 400 - self.radius:
			self.y_speed = -abs(self.y_speed)
		if self.y <= 0 + self.radius:
			self.y_speed = (abs(self.y_speed))
		
	def draw(self, canvas):
		'''Draw self on the canvas.'''

		canvas.create_oval(self.x-self.radius, self.y-self.radius, self.x + self.radius, self.y + self.radius, fill=self.color)

def addShape(event):
    '''Add new shapes where the user clicked.'''

    global game_objects
    game_objects.append(Circle(event.x, event.y))

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
    canvas = Tkinter.Canvas(root, width=400, height=400, background="black")
    canvas.pack()
    
    # if the user presses a key or the mouse, call our handlers
    root.bind('<Key-r>', reset)
    root.bind('<Button-1>', addShape)

    # start the draw loop
    draw(canvas)
    
    root.mainloop() # keep the window open

