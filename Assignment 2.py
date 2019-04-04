#Elijah Jefferson
#01/24/2019
#Draw multiple shapes and transform them using in place transformations
import math
from tkinter import *

CanvasWidth = 400
CanvasHeight = 400
d = 500

# ***************************** Initialize Objects ***************************
# Definition  of the five underlying points
pyapex = [150,200,100,1] #changed the pyramid to be in the upper right corner
pybase1 = [100,100,50,1]
pybase2 = [200,100,50,1]
pybase3 = [200,100,150,1]
pybase4 = [100,100,150,1]
#x and z values for apex are in the center
#half the distance between the difference in y values of apex and base is the center
pyCenter = [pyapex[0], pyapex[1] - (pyapex[1] - pybase1[1])/2, pyapex[2], 1]

#8 points for a cube in the top left
sqBase1 = [-150,250,50,1]
sqBase2 = [-50,250,50,1]
sqBase3 = [-50,250,150,1]
sqBase4 = [-150,250,150,1]
sqBase5 = [-150,150,50,1]
sqBase6 = [-50,150,50,1]
sqBase7 = [-50,150,150,1]
sqBase8 = [-150,150,150,1]
#half the difference in x, y, and z values of 1 and 7 is the center
#they are diagnal
sqCenter = [sqBase1[0] - (sqBase1[0] - sqBase7[0])/2, sqBase1[1] - (sqBase1[1] - sqBase7[1])/2, sqBase1[2] - (sqBase1[2] - sqBase7[2])/2, 1]

#Cube and Pyramid copies
py1apex = [150,0,100,1] 
py1base1 = [100,-100,50,1]
py1base2 = [200,-100,50,1]
py1base3 = [200,-100,150,1]
py1base4 = [100,-100,150,1]
#half the distance between the difference in y values of apex and base is the center
py1Center = [py1apex[0], py1apex[1] - (py1apex[1] - py1base1[1])/2, py1apex[2], 1]

sq1Base1 = [-150,-250,50,1]
sq1Base2 = [-50,-250,50,1]
sq1Base3 = [-50,-250,150,1]
sq1Base4 = [-150,-250,150,1]
sq1Base5 = [-150,-150,50,1]
sq1Base6 = [-50,-150,50,1]
sq1Base7 = [-50,-150,150,1]
sq1Base8 = [-150,-150,150,1]
#half the difference in x, y, and z values of 1 and 7 is the center
#they are diagnal
sq1Center = [sq1Base1[0] - (sq1Base1[0] - sq1Base7[0])/2, sq1Base1[1] - (sq1Base1[1] - sq1Base7[1])/2, sq1Base1[2] - (sq1Base1[2] - sq1Base7[2])/2, 1]

pydApex = [150,200,100,1] #default points for the top right pyramid
pydBase1 = [100,100,50,1]
pydBase2 = [200,100,50,1]
pydBase3 = [200,100,150,1]
pydBase4 = [100,100,150,1]
#half the distance between the difference in y values of apex and base is the center
pydCenter = [pydApex[0], pydApex[1] - (pydApex[1] - pydBase1[1])/2, pydApex[2], 1]

#Default points for the upper left cube
sqDBase1 = [-150,250,50,1]
sqDBase2 = [-50,250,50,1]
sqDBase3 = [-50,250,150,1]
sqDBase4 = [-150,250,150,1]
sqDBase5 = [-150,150,50,1]
sqDBase6 = [-50,150,50,1]
sqDBase7 = [-50,150,150,1]
sqDBase8 = [-150,150,150,1]
#half the difference in x, y, and z values of 1 and 7 is the center
#they are diagnal
sqDCenter = [sqDBase1[0] - (sqDBase1[0] - sqDBase7[0])/2, sqDBase1[1] - (sqDBase1[1] - sqDBase7[1])/2, sqDBase1[2] - (sqDBase1[2] - sqDBase7[2])/2, 1]

#Default points for the cube and pyramid copies
py1dApex = [150,0,100,1] 
py1dBase1 = [100,-100,50,1]
py1dBase2 = [200,-100,50,1]
py1dBase3 = [200,-100,150,1]
py1dBase4 = [100,-100,150,1]
#half the distance between the difference in y values of apex and base is the center
py1dCenter = [py1dApex[0], (py1dApex[1] - py1dBase1[1])/2, py1dApex[2], 1]

sq1DBase1 = [-150,-250,50,1]
sq1DBase2 = [-50,-250,50,1]
sq1DBase3 = [-50,-250,150,1]
sq1DBase4 = [-150,-250,150,1]
sq1DBase5 = [-150,-150,50,1]
sq1DBase6 = [-50,-150,50,1]
sq1DBase7 = [-50,-150,150,1]
sq1DBase8 = [-150,-150,150,1]
#half the difference in x, y, and z values of 1 and 7 is the center
#they are diagnal
sq1DCenter = [sq1DBase1[0] - (sq1DBase1[0] - sq1DBase7[0])/2, sq1DBase1[1] - (sq1DBase1[1] - sq1DBase7[1])/2, sq1DBase1[2] - (sq1DBase1[2] - sq1DBase7[2])/2, 1]
# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside

pyfrontpoly = [pyapex,pybase1,pybase2]
pyrightpoly = [pyapex,pybase2,pybase3]
pybackpoly = [pyapex,pybase3,pybase4]
pyleftpoly = [pyapex,pybase4,pybase1]
pybottompoly = [pybase4,pybase3,pybase2,pybase1]

#Polygons for the top left cube
sqFrontPoly = [sqBase1, sqBase2, sqBase6, sqBase5]
sqRightPoly = [sqBase2, sqBase6, sqBase7, sqBase3]
sqBackPoly = [sqBase1, sqBase2, sqBase6, sqBase5]
sqLeftPoly = [sqBase1, sqBase4, sqBase8, sqBase5]
sqBottomPoly = [sqBase1, sqBase2, sqBase3, sqBase4]
sqTopPoly = [sqBase5, sqBase6, sqBase7, sqBase8]

#Copy of the pyramid and cube polygons
py1frontpoly = [py1apex,py1base1,py1base2]
py1rightpoly = [py1apex,py1base2,py1base3]
py1backpoly = [py1apex,py1base3,py1base4]
py1leftpoly = [py1apex,py1base4,py1base1]
py1bottompoly = [py1base4,py1base3,py1base2,py1base1]

sq1FrontPoly = [sq1Base1, sq1Base2, sq1Base6, sq1Base5]
sq1RightPoly = [sq1Base2, sq1Base6, sq1Base7, sq1Base3]
sq1BackPoly = [sq1Base1, sq1Base2, sq1Base6, sq1Base5]
sq1LeftPoly = [sq1Base1, sq1Base4, sq1Base8, sq1Base5]
sq1BottomPoly = [sq1Base1, sq1Base2, sq1Base3, sq1Base4]
sq1TopPoly = [sq1Base5, sq1Base6, sq1Base7, sq1Base8]

# Definition of the objects
Pyramid = [pybottompoly, pyfrontpoly, pyrightpoly, pybackpoly, pyleftpoly]
Cube = [sqBottomPoly, sqFrontPoly, sqRightPoly, sqBackPoly, sqLeftPoly, sqTopPoly]
Pyramid1 = [py1bottompoly, py1frontpoly, py1rightpoly, py1backpoly, py1leftpoly]
Cube1 = [sq1BottomPoly, sq1FrontPoly, sq1RightPoly, sq1BackPoly, sq1LeftPoly, sq1TopPoly]

# Definition of the Pyramids'  and Cubes' underlying point clouds.  No structure, just the points.
# Also contains point clouds for default points
PyramidPointCloud = [pyapex, pybase1, pybase2, pybase3, pybase4, pyCenter]
CubePointCloud = [sqBase1, sqBase2, sqBase3, sqBase4, sqBase5, sqBase6, sqBase7, sqBase8, sqCenter]
DefaultPyramidCloud = [pydApex, pydBase1, pydBase2, pydBase3, pydBase4, pydCenter]
DefaultCubeCloud = [sqDBase1, sqDBase2, sqDBase3,sqDBase4, sqDBase5, sqDBase6, sqDBase7, sqDBase8, sqDCenter]
PyramidPointCloud1 = [py1apex, py1base1, py1base2, py1base3, py1base4, py1Center]
CubePointCloud1 = [sq1Base1, sq1Base2, sq1Base3, sq1Base4, sq1Base5, sq1Base6, sq1Base7, sq1Base8, sq1Center]
DefaultPyramidCloud1 = [py1dApex, py1dBase1, py1dBase2, py1dBase3, py1dBase4, py1dCenter]
DefaultCubeCloud1 = [sq1DBase1, sq1DBase2, sq1DBase3,sq1DBase4, sq1DBase5, sq1DBase6, sq1DBase7, sq1DBase8, sq1DCenter]

#Use a dictionary to keep track of the PointCloud being used
PointCloud = dict([(0,[PyramidPointCloud, DefaultPyramidCloud]), (1,[CubePointCloud, DefaultCubeCloud]),
                   (2,[PyramidPointCloud1, DefaultPyramidCloud1]), (3,[CubePointCloud1, DefaultCubeCloud1])])
#Start the scene with the defined objects
Scene = [Pyramid, Cube, Pyramid1, Cube1]
#************************************************************************************

# This function resets the pyramid to its original size and location in 3D space
# Note that shortcuts like "apex = [0,50,100]" will not work as they build new
# structures rather than modifying the existing Pyramid / PyramidPointCloud
def resetShape():
    global currDefCloud
    global currCloud
    for x in range(0, len(currCloud) - 1):
        for y in range(0, 3):
            currCloud[x][y] = currDefCloud[x][y]
            
# This function translates an object by some displacement.  The displacement is a 3D
# vector so the amount of displacement in each dimension can vary.
def translate(object, displacement):
    for point in object: #every point in the point cloud
        for i in range(0, len(displacement)): #add each coordinate together
            point[i] = point[i] + displacement[i]
# This function performs a simple uniform scale of an object assuming the object is
# centered at the origin.  The scalefactor is a scalar.
# For the following 4 methods I changed manipulating the points to creating a matrix multiplication method
def scale(object,scalefactor):
    for index in range(0, len(object) - 1): #every point in the point cloud
        #Use index to find the origin point from the point cloud
        #Find the difference in point on the origin and the point from the object to find how much to move the object
        #to the origin and how much to move the point back
        tX = object[-1][0]
        tY = object[-1][1]
        tZ = object[-1][2]
        translateO = [[1, 0, 0, 0], #this is used to translate the point to origin
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [-1 * tX, -1 * tY, -1 * tZ, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateO)[i]
        
        #Creates a matrix based on the scale factor
        scaleM = [[scalefactor, 0, 0, 0],
                  [0, scalefactor, 0, 0],
                  [0, 0, scalefactor, 0],
                  [0, 0, 0, 1]]
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])):
            object[index][i] = matrixMultiplication(temp, scaleM)[i]
        
        translateB = [[1, 0, 0, 0], #this matrix used to translate the point back to where it came from
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [tX, tY, tZ, 1]]
        for i in range(0, len(object[index])):
            object[index][i] = matrixMultiplication(object[index], translateB)[i]
        
        

# This function performs a rotation of an object about the Z axis (from +X to +Y)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CCW
# in a LHS when viewed from -Z [the location of the viewer in the standard postion]
def rotateZ(object,degrees):
    
    for index in range(0, len(object) - 1):
        #Use index to find the origin point from the point cloud
        #to the origin and how much to move the point back
        
        #Create points to move to origin (the last point is the center
        x1 = object[-1][0]
        y1 = object[-1][1] 
        z1 = object[-1][2]
        translateO = [[1, 0, 0, 0], #this is used to translate the point to origin
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [-1 * x1, -1 * y1, -1 *z1, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateO)[i]
    
        #Use rotate formula for z rotation        
        rotateZ = [[math.cos(math.radians(degrees)), math.sin(math.radians(degrees)), 0, 0],
                   [-1 * math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]]
        #make a temporary point for rotation
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])):
            object[index][i] = matrixMultiplication(temp, rotateZ)[i]
        
            
        translateB = [[1, 0, 0, 0], #this matrix used to translate the object[index] back to where it came from
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [x1, y1, z1, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateB)[i]

       
# This function performs a rotation of an object about the Y axis (from +Z to +X)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +Y looking toward the origin.
def rotateY(object,degrees):
    for index in range(0, len(object) - 1):
    
        #Use index to find the origin point from the point cloud
        #to the origin and how much to move the point back
        x1 = object[-1][0] 
        y1 = object[-1][1] 
        z1 = object[-1][2] 
        translateB = [[1, 0, 0, 0], #this matrix used to translate the point back to where it came from
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [x1, y1, z1, 1]]
        
        translateO = [[1, 0, 0, 0], #this is used to translate the point to origin
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [-1 * x1, -1 * y1, -1 * z1, 1]]
        rotateY = [[math.cos(math.radians(degrees)), 0, -1 * math.sin(math.radians(degrees)), 0],
                   [0, 1, 0, 0],
                   [math.sin(math.radians(degrees)), 0, math.cos(math.radians(degrees)), 0],
                   [0, 0, 0, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateO)[i]
        #Use rotate formula for y rotation
        #make a temporary point for rotation
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(temp, rotateY)[i]
        
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateB)[i]
        
        
        
# This function performs a rotation of an object about the X axis (from +Y to +Z)
# by 'degrees', assuming the object is centered at the origin.  The rotation is CW
# in a LHS when viewed from +X looking toward the origin.
def rotateX(object,degrees): 
    #rotate using formula for clockwise rotation
    
    for index in range(0, len(object) - 1):

        #Use index to find the origin point from the point cloud
        #to the origin and how much to move the point back
        x1 = object[-1][0]
        y1 = object[-1][1]
        z1 = object[-1][2]
        translateB = [[1, 0, 0, 0], #this matrix used to translate the point back to where it came from
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [x1, y1, z1, 1]]
        #Matrix based on x axis rotation
        rotateX = [[1, 0, 0, 0],
                   [0, math.cos(math.radians(degrees)), math.sin(math.radians(degrees)), 0],
                   [0, -1 * math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), 0],
                   [0, 0, 0, 1]]
        translateO = [[1, 0, 0, 0], #this is used to translate the point to origin
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [-1 * x1, -1 * y1, -1 * z1, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateO)[i]
        #Use rotate formula for y rotation
        #make a temporary point for rotation
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(temp, rotateX)[i]
        
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateB)[i]
        


#The function will draw every object in the scene by repeatedly calling drawObject on each object in the scene
def drawScene(scene):
    global shape
    for index in range(len(scene)):
        if(index == shape):
            color = "green"
        else:
            color = "blue"
        drawObject(scene[index], color)
        
# The function will draw an object by repeatedly calling drawPoly on each polygon in the object
def drawObject(object, color): #Overload the function to switch the point clouds when selecting shapes
    for poly in object: #draw a polygon for each polygon in the object array
        drawPoly(poly,color)

# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.


# This function converts from 3D to 2D (+ depth) using the perspective projection technique.  Note that it
# will return a NEW list of points.  We will not want to keep around the projected points in our object as
# they are only used in rendering
def project(point):
    ps = []
    #convert points to projection points using d(x or y)/(d + z)
    ps.append((point[0] * d) / (d + point[2])) #point x
    ps.append((point[1] * d) / (d + point[2])) #point y
    ps.append(point[2] / (d + point[2])) #point z
    return ps

# This function converts a 2D point to display coordinates in the tk system.  Note that it will return a
# NEW list of points.  We will not want to keep around the display coordinate points in our object as 
# they are only used in rendering.
def convertToDisplayCoordinates(point):
    displayXY = []
    #origin is at (0,400) and needs to be in the middle
    displayXY.append(point[0] + (CanvasHeight/2)) #move the x starting point to the middle
    displayXY.append(- 1 * point[1] + (CanvasWidth/2)) #move the y starting point to the middle
    return displayXY

#Multiply a 1x4 matrix and a 4x4 matrix
#This will be used to multiply a point by a transformation, rotation, or scale matrix
def matrixMultiplication(arr1, arr2):
    
    arr3 = [0, 0, 0,0] #a temporary array for storing the answer to return
    for i in range(4): #Keeps track of the columns of all 3 matrices
        for j in range(4): #The rows of the 4x4 matrix
            arr3[i] += (arr1[j] * arr2[j][i])
    return arr3
# **************************************************************************
# Everything below this point implements the interface
#made the reference to the point cloud global so the buttons could pick up the change in clouds
def reset():
    global currCloud
    w.delete(ALL)
    resetShape()
    drawScene(Scene)

def larger():
    global currCloud
    w.delete(ALL)
    scale(currCloud,1.1)
    drawScene(Scene)

def smaller():
    global currCloud
    w.delete(ALL)
    scale(currCloud,0.9)
    drawScene(Scene)

def forward():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[0,0,5])
    drawScene(Scene)

def backward():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[0,0,-5])
    drawScene(Scene)

def left():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[-5,0,0])
    drawScene(Scene)

def right():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[5,0,0])
    drawScene(Scene)

def up():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[0,5,0])
    drawScene(Scene)

def down():
    global currCloud
    w.delete(ALL)
    translate(currCloud,[0,-5,0])
    drawScene(Scene)

def xPlus():
    global currCloud
    w.delete(ALL)
    rotateX(currCloud,5)
    drawScene(Scene)

def xMinus():
    global currCloud
    w.delete(ALL)
    rotateX(currCloud,-5)
    drawScene(Scene)

def yPlus():
    global currCloud
    w.delete(ALL)
    rotateY(currCloud,5)
    drawScene(Scene)

def yMinus():
    global currCloud
    w.delete(ALL)
    rotateY(currCloud,-5)
    drawScene(Scene)

def zPlus():
    global currCloud
    w.delete(ALL)
    rotateZ(currCloud,5)
    drawScene(Scene)

def zMinus():
    global currCloud
    w.delete(ALL)
    rotateZ(currCloud,-5)
    drawScene(Scene)

#select the previous object in the scene or start over from the end
def prev(_event=None):
    global shape
    global currObject
    global currDefCloud
    global currCloud
    shape -= 1
    if(shape < 0):
        shape = len(Scene) - 1
    currObject = Scene[shape]
    currCloud = PointCloud[shape][0]
    currDefCloud = PointCloud[shape][1]
    drawScene(Scene)
    
#select the previous object in the scene or start over from the end
def next(_event=None):
    global shape
    global currObject
    global currDefCloud
    global currCloud
    shape += 1
    if(shape >= len(Scene)):
        shape = 0
    currObject = Scene[shape]
    currCloud = PointCloud[shape][0]
    currDefCloud = PointCloud[shape][1]
    drawScene(Scene)
    

    
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight, background='black')
#Use a currObject to keep track of what object is being selected
shape = 0 #this is a global variable for the current object in the scene being used
currObject = Scene[shape]
currCloud = PointCloud[shape][0]
currDefCloud = PointCloud[shape][1]
#Test Draw Cube instead of Pyramid
w.delete(ALL)
w.pack()
drawScene(Scene)

controlpanel = Frame(outerframe)
controlpanel.pack()

resetcontrols = Frame(controlpanel, height=100, borderwidth=2, relief=RIDGE)
resetcontrols.pack(side=LEFT)

resetcontrolslabel = Label(resetcontrols, text="Reset")
resetcontrolslabel.pack()

resetButton = Button(resetcontrols, text="Reset", fg="green", command=reset)
resetButton.pack(side=LEFT)

scalecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
scalecontrols.pack(side=LEFT)

scalecontrolslabel = Label(scalecontrols, text="Scale")
scalecontrolslabel.pack()

largerButton = Button(scalecontrols, text="Larger", command=larger)
largerButton.pack(side=LEFT)

smallerButton = Button(scalecontrols, text="Smaller", command=smaller)
smallerButton.pack(side=LEFT)

translatecontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
translatecontrols.pack(side=LEFT)

translatecontrolslabel = Label(translatecontrols, text="Translation")
translatecontrolslabel.pack()

forwardButton = Button(translatecontrols, text="FW", command=forward)
forwardButton.pack(side=LEFT)

backwardButton = Button(translatecontrols, text="BK", command=backward)
backwardButton.pack(side=LEFT)

leftButton = Button(translatecontrols, text="LF", command=left)
leftButton.pack(side=LEFT)

rightButton = Button(translatecontrols, text="RT", command=right)
rightButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="UP", command=up)
upButton.pack(side=LEFT)

upButton = Button(translatecontrols, text="DN", command=down)
upButton.pack(side=LEFT)

rotationcontrols = Frame(controlpanel, borderwidth=2, relief=RIDGE)
rotationcontrols.pack(side=LEFT)

rotationcontrolslabel = Label(rotationcontrols, text="Rotation")
rotationcontrolslabel.pack()

xPlusButton = Button(rotationcontrols, text="X+", command=xPlus)
xPlusButton.pack(side=LEFT)

xMinusButton = Button(rotationcontrols, text="X-", command=xMinus)
xMinusButton.pack(side=LEFT)

yPlusButton = Button(rotationcontrols, text="Y+", command=yPlus)
yPlusButton.pack(side=LEFT)

yMinusButton = Button(rotationcontrols, text="Y-", command=yMinus)
yMinusButton.pack(side=LEFT)

zPlusButton = Button(rotationcontrols, text="Z+", command=zPlus)
zPlusButton.pack(side=LEFT)

zMinusButton = Button(rotationcontrols, text="Z-", command=zMinus)
zMinusButton.pack(side=LEFT)

#Use buttons to select the shape in the scene

root.bind('<Left>', prev)
root.bind('<Right>', next)

root.mainloop()