import sys

try:
    from OpenGL.GLUT import *
    from OpenGL.GL import *
    from OpenGL.GLU import *
    from OpenGL.GL import glOrtho
    from OpenGL.GLU import gluPerspective
    from OpenGL.GL import glRotated
    from OpenGL.GL import glTranslated
    from OpenGL.GL import glLoadIdentity
    from OpenGL.GL import glMatrixMode
    from OpenGL.GL import GL_MODELVIEW
    from OpenGL.GL import GL_PROJECTION
except:
    print("ERROR: PyOpenGL not installed properly. ")

DISPLAY_WIDTH = 500.0
DISPLAY_HEIGHT = 500.0
Xdisp = 0
Ydisp = 0
Zdisp = 0
Rotate = 0

Ztire = -15
tireRotate = 0

PERSPECTIVE = 'p'


def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

 
def drawCar():
    glLineWidth(2.5)
    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-3, 2, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 2, 2)
    #Back Side
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 1, -2)
    glVertex3f(-3, 2, -2)
    #Connectors
    glVertex3f(-3, 2, 2)
    glVertex3f(-3, 2, -2)
    glVertex3f(-2, 3, 2)
    glVertex3f(-2, 3, -2)
    glVertex3f(2, 3, 2)
    glVertex3f(2, 3, -2)
    glVertex3f(3, 2, 2)
    glVertex3f(3, 2, -2)
    glVertex3f(3, 1, 2)
    glVertex3f(3, 1, -2)
    glVertex3f(-3, 1, 2)
    glVertex3f(-3, 1, -2)
    glEnd()
    
def drawTire():
    glLineWidth(2.5)
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_LINES)
    #Front Side
    glVertex3f(-1, .5, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, .5, .5)
    #Back Side
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, -.5, -.5)
    glVertex3f(-1, .5, -.5)
    #Connectors
    glVertex3f(-1, .5, .5)
    glVertex3f(-1, .5, -.5)
    glVertex3f(-.5, 1, .5)
    glVertex3f(-.5, 1, -.5)
    glVertex3f(.5, 1, .5)
    glVertex3f(.5, 1, -.5)
    glVertex3f(1, .5, .5)
    glVertex3f(1, .5, -.5)
    glVertex3f(1, -.5, .5)
    glVertex3f(1, -.5, -.5)
    glVertex3f(.5, -1, .5)
    glVertex3f(.5, -1, -.5)
    glVertex3f(-.5, -1, .5)
    glVertex3f(-.5, -1, -.5)
    glVertex3f(-1, -.5, .5)
    glVertex3f(-1, -.5, -.5)
    glEnd()

def drawHouse ():
    glLineWidth(2.5)
    glColor3f(1.0, 0.0, 0.0)
    #Floor
    glBegin(GL_LINES)
    glVertex3f(-5.0, 0.0, -5.0)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 0, -5)
    #Ceiling
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 5, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, 5)
    glVertex3f(-5, 5, -5)
    #Walls
    glVertex3f(-5, 0, -5)
    glVertex3f(-5, 5, -5)
    glVertex3f(5, 0, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(5, 0, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(-5, 0, 5)
    glVertex3f(-5, 5, 5)
    #Door
    glVertex3f(-1, 0, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(-1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 3, 5)
    glVertex3f(1, 0, 5)
    #Roof
    glVertex3f(-5, 5, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(0, 8, -5)
    glVertex3f(5, 5, -5)
    glVertex3f(-5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(5, 5, 5)
    glVertex3f(0, 8, 5)
    glVertex3f(0, 8, -5)
    glEnd()

def start ():
    global Xdisp
    global Zdisp
    global Ydisp
    global Rotate
    global Ztire
    global tireRotate

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Zdisp = 0
    Xdisp = 0
    Ydisp = 0
    Rotate = 0
    Ztire = -15
    tireRotate = 0
def display():
    import math
    global PERSPECTIVE
    global Ztire
    global tireRotate
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 
    #Your Code Here

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if PERSPECTIVE == 'p':
        gluPerspective(90, 1, 1, 250)
    else:
        glOrtho(-10, 10, -10, 10, 1, 100)

    glMatrixMode(GL_MODELVIEW)
    drawHouse()

    glPushMatrix()
    glTranslatef(Ztire, 0, 15)
    drawCar()
    glTranslatef(-2, 0, -2)
    glRotatef(tireRotate, 0, 0, 1)
    drawTire()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(Ztire-2, 0, 15+2)
    glRotatef(tireRotate, 0, 0, 1)
    drawTire()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(Ztire+2, 0, 15+2)
    glRotatef(tireRotate, 0, 0, 1)
    drawTire()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(Ztire+2, 0, 15-2)
    glRotatef(tireRotate, 0, 0, 1)
    drawTire()

    glPopMatrix()
    glPushMatrix()
    glTranslated(-20, 0, 0)
    drawHouse()
    glRotated(90, 0, 1, 0)
    glTranslated(-20, 0, -20)
    drawHouse()
    glTranslated(-20, 0, 20)
    glRotated(90, 0, 1, 0)
    drawHouse()
    glTranslated(-20, 0, 0)
    drawHouse()
    glTranslated(-20, 0, 0)
    drawHouse()
    glTranslated(-20, 0, 0)
    drawHouse()
    glRotated(180, 0, 1, 0)
    glTranslated(0, 0, -40)
    drawHouse()
    glTranslated(-20, 0, 0)
    drawHouse()
    glPopMatrix()    
    glFlush()
    
def timer(n):
    global Ztire
    global tireRotate
    Ztire += .1
    tireRotate -= 1.5
    if tireRotate < 0:
        tireRotate += 360
    glutPostRedisplay()
    glutTimerFunc(25, timer, 1)

def keyboard(key, x, y):
    import math
    global Xdisp
    global Ydisp
    global Zdisp
    global Rotate
    global PERSPECTIVE
    if key == chr(27):
        import sys
        sys.exit(0)

    if key == b'w':
        Xdisp += math.sin(math.radians(Rotate))
        Zdisp += math.cos(math.radians(Rotate))
        glTranslated(math.sin(math.radians(Rotate)), 0, math.cos(math.radians(Rotate)))


    if key == b'a':
        Xdisp += math.cos(math.radians(Rotate))
        Zdisp -= math.sin(math.radians(Rotate))
        glTranslated(math.cos(math.radians(Rotate)), 0, -math.sin(math.radians(Rotate)))

    if key == b'd':
        Xdisp -= math.cos(math.radians(Rotate))
        Zdisp += math.sin(math.radians(Rotate))
        glTranslated(-math.cos(math.radians(Rotate)), 0, math.sin(math.radians(Rotate)))

    if key == b's':
        Xdisp -= math.sin(math.radians(Rotate))
        Zdisp -= math.cos(math.radians(Rotate))
        glTranslated(-math.sin(math.radians(Rotate)),0,-math.cos(math.radians(Rotate)))

    if key == b'q':
        Rotate += 1
        if Rotate > 360:
            Rotate -= 360
        glTranslated(-Xdisp, 0, -Zdisp)
        glRotated(-1, 0, 1, 0)
        glTranslated(Xdisp, 0, Zdisp)


    if key == b'e':
        Rotate -= 1
        if Rotate < 0:
            Rotate += 360

        glTranslated(-Xdisp, 0, -Zdisp)
        glRotated(1,0, 1, 0)
        glTranslated(Xdisp, 0, Zdisp)

    if key == b'r':
        glTranslated(0,-1,0)

    if key == b'f':
        glTranslated(0,1,0)

    if key == b'h':
        start()

    if key == b'o':
        PERSPECTIVE = 'o'

    if key == b'p':    
        PERSPECTIVE = 'p'  
    #Your Code Here
  
    glutPostRedisplay()


glutInit(sys.argv)
glutInitDisplayMode (GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize (int(DISPLAY_WIDTH), int(DISPLAY_HEIGHT))
glutInitWindowPosition (100, 100)
glutCreateWindow (b'OpenGL Lab')
init ()
start()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutTimerFunc(25, timer, 1)
glutMainLoop()
