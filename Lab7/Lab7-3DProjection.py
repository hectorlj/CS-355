# Import a library of functions called 'pygame'
import pygame
from math import pi
import numpy as np
import math as m

class Point:
	def __init__(self,x,y):
		self.x = x
		self.y = y

class Point3D:
	def __init__(self,x,y,z):
		self.x = x
		self.y = y
		self.z = z
		
class Line3D():
	
	def __init__(self, start, end):
		self.start = start
		self.end = end

def loadOBJ(filename):
	
	vertices = []
	indices = []
	lines = []
	
	f = open(filename, "r")
	for line in f:
		t = str.split(line)
		if not t:
			continue
		if t[0] == "v":
			vertices.append(Point3D(float(t[1]),float(t[2]),float(t[3])))
			
		if t[0] == "f":
			for i in range(1,len(t) - 1):
				index1 = int(str.split(t[i],"/")[0])
				index2 = int(str.split(t[i+1],"/")[0])
				indices.append((index1,index2))
			
	f.close()
	
	#Add faces as lines
	for index_pair in indices:
		index1 = index_pair[0]
		index2 = index_pair[1]
		lines.append(Line3D(vertices[index1 - 1],vertices[index2 - 1]))
		
	#Find duplicates
	duplicates = []
	for i in range(len(lines)):
		for j in range(i+1, len(lines)):
			line1 = lines[i]
			line2 = lines[j]
			
			# Case 1 -> Starts match
			if line1.start.x == line2.start.x and line1.start.y == line2.start.y and line1.start.z == line2.start.z:
				if line1.end.x == line2.end.x and line1.end.y == line2.end.y and line1.end.z == line2.end.z:
					duplicates.append(j)
			# Case 2 -> Start matches end
			if line1.start.x == line2.end.x and line1.start.y == line2.end.y and line1.start.z == line2.end.z:
				if line1.end.x == line2.start.x and line1.end.y == line2.start.y and line1.end.z == line2.start.z:
					duplicates.append(j)
					
	duplicates = list(set(duplicates))
	duplicates.sort()
	duplicates = duplicates[::-1]
	
	#Remove duplicates
	for j in range(len(duplicates)):
		del lines[duplicates[j]]
	
	return lines

def loadHouse():
    house = []
    #Floor
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(5, 0, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 0, 5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(-5, 0, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 0, -5)))
    #Ceiling
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 5, -5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(5, 5, 5), Point3D(-5, 5, 5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(-5, 5, -5)))
    #Walls
    house.append(Line3D(Point3D(-5, 0, -5), Point3D(-5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(5, 0, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(-5, 0, 5), Point3D(-5, 5, 5)))
    #Door
    house.append(Line3D(Point3D(-1, 0, 5), Point3D(-1, 3, 5)))
    house.append(Line3D(Point3D(-1, 3, 5), Point3D(1, 3, 5)))
    house.append(Line3D(Point3D(1, 3, 5), Point3D(1, 0, 5)))
    #Roof
    house.append(Line3D(Point3D(-5, 5, -5), Point3D(0, 8, -5)))
    house.append(Line3D(Point3D(0, 8, -5), Point3D(5, 5, -5)))
    house.append(Line3D(Point3D(-5, 5, 5), Point3D(0, 8, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(5, 5, 5)))
    house.append(Line3D(Point3D(0, 8, 5), Point3D(0, 8, -5)))
	
    return house

def loadCar():
    car = []
    #Front Side
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-2, 3, 2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(2, 3, 2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(3, 2, 2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 1, 2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(-3, 1, 2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 2, 2)))

    #Back Side
    car.append(Line3D(Point3D(-3, 2, -2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(-2, 3, -2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, -2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 2, -2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(3, 1, -2), Point3D(-3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, -2), Point3D(-3, 2, -2)))
    
    #Connectors
    car.append(Line3D(Point3D(-3, 2, 2), Point3D(-3, 2, -2)))
    car.append(Line3D(Point3D(-2, 3, 2), Point3D(-2, 3, -2)))
    car.append(Line3D(Point3D(2, 3, 2), Point3D(2, 3, -2)))
    car.append(Line3D(Point3D(3, 2, 2), Point3D(3, 2, -2)))
    car.append(Line3D(Point3D(3, 1, 2), Point3D(3, 1, -2)))
    car.append(Line3D(Point3D(-3, 1, 2), Point3D(-3, 1, -2)))

    return car

def loadTire():
    tire = []
    #Front Side
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-.5, 1, .5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(.5, 1, .5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(1, .5, .5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, -.5, .5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(.5, -1, .5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(-.5, -1, .5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-1, -.5, .5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, .5, .5)))

    #Back Side
    tire.append(Line3D(Point3D(-1, .5, -.5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, -.5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, -.5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, .5, -.5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, -.5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(.5, -1, -.5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, -.5), Point3D(-1, -.5, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, -.5), Point3D(-1, .5, -.5)))

    #Connectors
    tire.append(Line3D(Point3D(-1, .5, .5), Point3D(-1, .5, -.5)))
    tire.append(Line3D(Point3D(-.5, 1, .5), Point3D(-.5, 1, -.5)))
    tire.append(Line3D(Point3D(.5, 1, .5), Point3D(.5, 1, -.5)))
    tire.append(Line3D(Point3D(1, .5, .5), Point3D(1, .5, -.5)))
    tire.append(Line3D(Point3D(1, -.5, .5), Point3D(1, -.5, -.5)))
    tire.append(Line3D(Point3D(.5, -1, .5), Point3D(.5, -1, -.5)))
    tire.append(Line3D(Point3D(-.5, -1, .5), Point3D(-.5, -1, -.5)))
    tire.append(Line3D(Point3D(-1, -.5, .5), Point3D(-1, -.5, -.5)))
    
    return tire

def homogenousLines(model):
	linelist = []
	for s in model:
		linelist.append(Line3D([s.start.x, s.start.y, s.start.z, 1], [s.end.x, s.end.y, s.end.z, 1]))
	return linelist

def objectToWorld(model, places):
	linelist = []
	for i in places:
		for s in model:
			var = i.dot(s.start)
			var2 = i.dot(s.end)
			linelist.append(Line3D(var, var2))
	return linelist

def worldToCamera(modellist, x, y, z, rotation):
	camera = np.array([
						[[1,0,0,x],
						 [0,1,0,y],
						 [0,0,1,z],
						 [0,0,0,1]],

						[[m.cos(m.radians(rotation)),0,-m.sin(m.radians(rotation)),0],
						 [0,1,0,0],
						 [m.sin(m.radians(rotation)),0,m.cos(m.radians(rotation)),0],
						 [0,0,0,1]]
					])
	linelist = []
	for s in modellist:
		var = camera[0].dot(s.start)
		var = camera[1].dot(var)
		var2 = camera[0].dot(s.end)
		var2 = camera[1].dot(var2)
		linelist.append(Line3D(var, var2))
	return linelist

def clipView(modellist):
	linelist = []
	for s in modellist:
		var = clip.dot(s.start)
		var2 = clip.dot(s.end)
		w = var[3]
		w2 = var2[3]

		x = var[0]
		y = var[1]
		z = var[2]
		x2 = var2[0]
		y2 = var2[1]
		z2 = var2[2]
		if not ((x < -w and x2 < -w2) or (y < -w and y2 < -w2) or (z2 < -w2 or z < -w) or
			(x > w and x2 > w2) or (y > w and y2 > w2) or (z2 > w2 and z > w)):
			# print('x, y, z, w')
			# print(var)
			# print('2 x, y, z, w 2')
			# print(var2)
			# print(y>w)
			# print(y2 >w2)
		# if not (( x > w and x2 > w2) or (y2 > w2 and  y > w) and (z > w and z2 > w2)) 
			linelist.append(Line3D(var, var2))
	return linelist

def cut(modellist):
	linelist = []
	for s in modellist:
		var = s.start/s.start[3]
		var2 = s.end/s.end[3]
		linelist.append(Line3D([var[0], var[1], 1], [var2[0], var2[1], 1]))
	return linelist

def toView(modellist):
	linelist = []
	for s in modellist:
		var = screenview.dot(s.start)
		var2 = screenview.dot(s.end)
		linelist.append(Line3D([var[0], var[1]], [var2[0], var2[1]]))
	return linelist

def drawHouse(linelist, x, y, z, rotation):
	linelist2 = homogenousLines(linelist)
	linelist3 = objectToWorld(linelist2, houses)
	linelist4 = worldToCamera(linelist3, x, y, z, rotation)
	linelist5 = clipView(linelist4)
	linelist6 = cut(linelist5)
	linelist7 = toView(linelist6)
	for s in linelist7:
		pygame.draw.line(screen, BLUE, (s.start[0], s.start[1]), (s.end[0], s.end[1]))

def drawCar(linelist, x, y, z, rotation):
	linelist2 = homogenousLines(linelist)
	linelist3 = objectToWorld(linelist2, car)
	linelist4 = worldToCamera(linelist3, x, y, z, rotation)
	linelist5 = clipView(linelist4)
	linelist6 = cut(linelist5)
	linelist7 = toView(linelist6)
	for s in linelist7:
		pygame.draw.line(screen, GREEN, (s.start[0], s.start[1]), (s.end[0], s.end[1]))

def drawTires(linelist, x, y, z, rotation):
	linelist2 = homogenousLines(linelist)
	linelist3 = objectToWorld(linelist2, tires)
	linelist4 = worldToCamera(linelist3, x, y, z, rotation)
	linelist5 = clipView(linelist4)
	linelist6 = cut(linelist5)
	linelist7 = toView(linelist6)
	for s in linelist7:
		pygame.draw.line(screen, RED, (s.start[0], s.start[1]), (s.end[0], s.end[1]))

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Set the height and width of the screen
size = [500, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Shape Drawing")
 
#Set needed variables
done = False
clock = pygame.time.Clock()
start = Point(0.0,0.0)
end = Point(0.0,0.0)
near = .0001
far = 1000
f = 90
linelist = loadHouse()
carLineList = loadCar()
tireLineList = loadTire()
Xdisp = 0
Zdisp = 0
Ydisp = -5
Rotate = 0
den = far-near
clip1 = (far+near)/den
clip2 = (-2*far*near)/den
zoom = 1/m.tan(m.radians(f/2))
houses = np.array([
						[[m.cos(pi),0,-m.sin(pi),0],
						 [0,1,0,0],
						 [m.sin(pi),0,m.cos(pi),20],
						 [0,0,0,1]],

						[[m.cos(pi),0,-m.sin(pi),15],
						 [0,1,0,0],
						 [m.sin(pi),0,m.cos(pi),20],
						 [0,0,0,1]],

						[[m.cos(pi),0,-m.sin(pi),-15],
						 [0,1,0,0],
						 [m.sin(pi),0,m.cos(pi),20],
						 [0,0,0,1]],

						[[1,0,0,0],
						 [0,1,0,0],
						 [0,0,1,-20],
						 [0,0,0,1]],

						[[1,0,0,15],
						 [0,1,0,0],
						 [0,0,1,-20],
						 [0,0,0,1]],

						[[1,0,0,-15],
						 [0,1,0,0],
						 [0,0,1,-20],
						 [0,0,0,1]],

						[[m.cos(3*pi/2),0,-m.sin(3*pi/2),-25],
						 [0,1,0,0],
						 [m.sin(3*pi/2),0,m.cos(3*pi/2), 0],
						 [0,0,0,1]]
					])

car = np.array([
				[[1,0,0,0],
				 [0,1,0,0],
				 [0,0,1,10],
				 [0,0,0,1]]
				])

tires = np.array([
				[[1,0,0,2],
				 [0,1,0,0],
				 [0,0,1,12],
				 [0,0,0,1]],

				[[1,0,0,-2],
				 [0,1,0,0],
				 [0,0,1,12],
				 [0,0,0,1]],

				[[1,0,0,2],
				 [0,1,0,0],
				 [0,0,1,8],
				 [0,0,0,1]],

				[[1,0,0,-2],
				 [0,1,0,0],
				 [0,0,1,8],
				 [0,0,0,1]]
				])


clip = np.array([[1.73, 0, 0, 0],
					[0, 1.73, 0, 0],
					[0, 0, clip1, clip2],
					[0, 0, 1, 0]])

screenview = np.array([[512/2, 0, 512/2],
						[0, -512/2, 512/2],
						[0,0,1]])

#Loop until the user clicks the close button.
while not done:
 
	# This limits the while loop to a max of 100 times per second.
	# Leave this out and we will use all CPU we can.
	clock.tick(100)

	# Clear the screen and set the screen background
	screen.fill(BLACK)

	#Controller Code#
	#####################################################################

	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
			done=True
			
	pressed = pygame.key.get_pressed()


	if pressed[pygame.K_a]:
		# c("a is pressed")
		Xdisp += m.cos(m.radians(Rotate))
		Zdisp -= m.sin(m.radians(Rotate))

	if pressed[pygame.K_w]:
		# c("w is pressed")
		Xdisp -= m.sin(m.radians(Rotate))
		Zdisp -= m.cos(m.radians(Rotate))

	if pressed[pygame.K_d]:
		# c("d is pressed")
		Xdisp -= m.cos(m.radians(Rotate))
		Zdisp += m.sin(m.radians(Rotate))

	if pressed[pygame.K_s]:
		# c("s is pressed")
		Xdisp += m.sin(m.radians(Rotate))
		Zdisp += m.cos(m.radians(Rotate))

	if pressed[pygame.K_q]:
		# c("q is pressed")
		Rotate -= 1
		if Rotate < 0:
			Rotate += 360

	if pressed[pygame.K_e]:
		# c("e is pressed")
		Rotate += 1
		if Rotate > 360:
			Rotate -= 360

	if pressed[pygame.K_r]:
		# c("r is pressed")
		Ydisp -= 1

	if pressed[pygame.K_f]:
		# c("f is pressed")
		Ydisp += 1

	if pressed[pygame.K_h]:
		# c("h is pressed")
		linelist = loadHouse()
		carLineList = loadCar()
		tireLineList = loadTire()
		Xdisp = 0
		Zdisp = 0
		Ydisp = -5
		Rotate = 0

	#Viewer Code#
	#####################################################################
	drawHouse(linelist, Xdisp, Ydisp, Zdisp, Rotate)
	drawCar(carLineList, Xdisp, Ydisp, Zdisp, Rotate)
	drawTires(tireLineList, Xdisp, Ydisp, Zdisp, Rotate)

	# Go ahead and update the screen with what we've drawn.
	# This MUST happen after all the other drawing commands.
	pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
