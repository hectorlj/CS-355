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
PERSPECTIVE = 'p'


def init(): 
    glClearColor (0.0, 0.0, 0.0, 0.0)
    glShadeModel (GL_FLAT)

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
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    Zdisp = 0
    Xdisp = 0
    Ydisp = 0
    Rotate = 0
def display():
    global PERSPECTIVE
    glClear (GL_COLOR_BUFFER_BIT)
    glColor3f (1.0, 1.0, 1.0)
    # viewing transformation 
    #Your Code Here

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if PERSPECTIVE == 'p':
        gluPerspective(90, 1, 1, 50)
    else:
        glOrtho(-10, 10, -10, 10, 1, 100)

    glMatrixMode(GL_MODELVIEW)
    drawHouse()

    
    glFlush()
    

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
        print('W is pressed')
        Xdisp += math.sin(math.radians(Rotate))
        Zdisp += math.cos(math.radians(Rotate))
        glTranslated(math.sin(math.radians(Rotate)), 0, math.cos(math.radians(Rotate)))


    if key == b'a':
        print('A is pressed')
        Xdisp += math.cos(math.radians(Rotate))
        Zdisp -= math.sin(math.radians(Rotate))
        glTranslated(math.cos(math.radians(Rotate)), 0, -math.sin(math.radians(Rotate)))

    if key == b'd':
        print('D is pressed')
        Xdisp -= math.cos(math.radians(Rotate))
        Zdisp += math.sin(math.radians(Rotate))
        glTranslated(-math.cos(math.radians(Rotate)), 0, math.sin(math.radians(Rotate)))

    if key == b's':
        print('S is pressed')
        Xdisp -= math.sin(math.radians(Rotate))
        Zdisp -= math.cos(math.radians(Rotate))
        glTranslated(-math.sin(math.radians(Rotate)),0,-math.cos(math.radians(Rotate)))

    if key == b'q':
        print('Q is pressed')
        Rotate += 1
        if Rotate > 360:
            Rotate -= 360
        glTranslated(-Xdisp, 0, -Zdisp)
        glRotated(-1, 0, 1, 0)
        glTranslated(Xdisp, 0, Zdisp)


    if key == b'e':
        print('E is pressed')
        Rotate -= 1
        if Rotate < 0:
            Rotate += 360

        glTranslated(-Xdisp, 0, -Zdisp)
        glRotated(1,0, 1, 0)
        glTranslated(Xdisp, 0, Zdisp)

    if key == b'r':
        print('R is pressed')
        glTranslated(0,-1,0)

    if key == b'f':
        print('F is pressed')
        glTranslated(0,1,0)

    if key == b'h':
        print("H is pressed")
        start()

    if key == b'o':
        print("O is pressed")
        PERSPECTIVE = 'o'

    if key == b'p':
        print("P is pressed")    
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
glutMainLoop()
