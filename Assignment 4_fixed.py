#Elijah Jefferson
#02/01/2019
#Add lighting and shading to a cylinder
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
sqBase1 = [-150,150,50,1]
sqBase2 = [-50,150,50,1]
sqBase3 = [-50,150,150,1]
sqBase4 = [-150,150,150,1]
sqBase5 = [-150,50,50,1]
sqBase6 = [-50,50,50,1]
sqBase7 = [-50,50,150,1]
sqBase8 = [-150,50,150,1]
#half the difference in x, y, and z values of 1 and 7 is the center
#they are diagnal
sqCenter = [sqBase1[0] - (sqBase1[0] - sqBase7[0])/2, sqBase1[1] - (sqBase1[1] - sqBase7[1])/2, sqBase1[2] - (sqBase1[2] - sqBase7[2])/2, 1]

#Pyramid copy
py1apex = [150,0,100,1] 
py1base1 = [100,-100,50,1]
py1base2 = [200,-100,50,1]
py1base3 = [200,-100,150,1]
py1base4 = [100,-100,150,1]
#half the distance between the difference in y values of apex and base is the center
py1Center = [py1apex[0], py1apex[1] - (py1apex[1] - py1base1[1])/2, py1apex[2], 1]

#make a cylinde of 8 rectangles by drawing 2 octogons
cyTop1 = [-150, -100, 50,1]
cyTop2 = [-130, -100, 50,1]
cyTop3 = [-130 + math.sin(45) * 20, -100, 50 + math.sin(45) * 20,1]
cyTop4 = [-130 + math.sin(45) * 20, -100, 70 + math.sin(45) * 20,1]
cyTop5 = [-130, -100, 70 + math.sin(45) * 40,1]
cyTop6 = [-150, -100, 70 + math.sin(45) * 40,1]
cyTop7 = [-150 - math.sin(45) * 20, -100, 70 + math.sin(45) * 20,1]
cyTop8 = [-150 - math.sin(45) * 20, -100, 50 + math.sin(45) * 20,1]
cyBottom1 = [-150, -200, 50,1]
cyBottom2 = [-130, -200, 50,1]
cyBottom3 = [-130 + math.sin(45) * 20, -200, 50 + math.sin(45) * 20,1]
cyBottom4 = [-130 + math.sin(45) * 20, -200, 70 + math.sin(45) * 20,1]
cyBottom5 = [-130, -200, 70 + math.sin(45) * 40,1]
cyBottom6 = [-150, -200, 70 + math.sin(45) * 40,1]
cyBottom7 = [-150 - math.sin(45) * 20, -200, 70 + math.sin(45) * 20,1]
cyBottom8 = [-150 - math.sin(45) * 20, -200, 50 + math.sin(45) * 20,1]
#center point is the mid point of 8 and 3, any y value from top and bottom, and 2 and 5
cyCenter = [cyTop8[0] - (cyTop8[0] - cyTop3[0])/2, cyTop1[1] - (cyTop1[1] - cyBottom1[1])/2, cyTop2[2] + (cyTop5[2] - cyTop2[2])/2 ,1]

pydApex = [150,200,100,1] #default points for the top right pyramid
pydBase1 = [100,100,50,1]
pydBase2 = [200,100,50,1]
pydBase3 = [200,100,150,1]
pydBase4 = [100,100,150,1]
#half the distance between the difference in y values of apex and base is the center
pydCenter = [pydApex[0], pydApex[1] - (pydApex[1] - pydBase1[1])/2, pydApex[2], 1]

#Default points for the upper left cube
sqDBase1 = [-150,150,50,1]
sqDBase2 = [-50,150,50,1]
sqDBase3 = [-50,150,150,1]
sqDBase4 = [-150,150,150,1]
sqDBase5 = [-150,50,50,1]
sqDBase6 = [-50,50,50,1]
sqDBase7 = [-50,50,150,1]
sqDBase8 = [-150,50,150,1]
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

cydTop1 = [-150, -100, 50,1]
cydTop2 = [-130, -100, 50,1]
cydTop3 = [-130 + math.sin(45) * 20, -100, 50 + math.sin(45) * 20,1]
cydTop4 = [-130 + math.sin(45) * 20, -100, 70 + math.sin(45) * 20,1]
cydTop5 = [-130, -100, 70 + math.sin(45) * 40,1]
cydTop6 = [-150, -100, 70 + math.sin(45) * 40,1]
cydTop7 = [-150 - math.sin(45) * 20, -100, 70 + math.sin(45) * 20,1]
cydTop8 = [-150 - math.sin(45) * 20, -100, 50 + math.sin(45) * 20,1]
cydBottom1 = [-150, -200, 50,1]
cydBottom2 = [-130, -200, 50,1]
cydBottom3 = [-130 + math.sin(45) * 20, -200, 50 + math.sin(45) * 20,1]
cydBottom4 = [-130 + math.sin(45) * 20, -200, 70 + math.sin(45) * 20,1]
cydBottom5 = [-130, -200, 70 + math.sin(45) * 40,1]
cydBottom6 = [-150, -200, 70 + math.sin(45) * 40,1]
cydBottom7 = [-150 - math.sin(45) * 20, -200, 70 + math.sin(45) * 20,1]
cydBottom8 = [-150 - math.sin(45) * 20, -200, 50 + math.sin(45) * 20,1]
#center point is the mid point of 8 and 3, any y value from top and bottom, and 2 and 5
cydCenter = [cydTop8[0] - (cydTop8[0] - cydTop3[0])/2, cydTop1[1] - (cydTop1[1] - cydBottom1[1])/2, cydTop2[2] + (cydTop5[2] - cydTop2[2])/2 ,1]

# Definition of the five polygon faces using the meaningful point names
# Polys are defined in counter clockwise order when viewed from the outside

pyfrontpoly = [pyapex,pybase1,pybase2]
pyrightpoly = [pyapex,pybase2,pybase3]
pybackpoly = [pyapex,pybase3,pybase4]
pyleftpoly = [pyapex,pybase4,pybase1]
pybottompoly = [pybase4,pybase3,pybase2,pybase1]

#Polygons for the top left cube
sqFrontPoly = [sqBase2, sqBase1, sqBase5, sqBase6]
sqRightPoly = [sqBase3, sqBase2, sqBase6, sqBase7]
sqBackPoly = [sqBase4, sqBase3, sqBase7, sqBase8]
sqLeftPoly = [sqBase4, sqBase8, sqBase5, sqBase1]
sqTopPoly = [sqBase3, sqBase4, sqBase1, sqBase2]
sqBottomPoly = [sqBase8, sqBase7, sqBase6, sqBase5]

#Copy of the pyramid and cube polygons
py1frontpoly = [py1apex,py1base1,py1base2]
py1rightpoly = [py1apex,py1base2,py1base3]
py1backpoly = [py1apex,py1base3,py1base4]
py1leftpoly = [py1apex,py1base4,py1base1]
py1bottompoly = [py1base4,py1base3,py1base2,py1base1]

#polygons for the cylinder
cyPoly12 = [cyTop1, cyBottom1, cyBottom2, cyTop2]
cyPoly23 = [cyTop2, cyBottom2, cyBottom3, cyTop3]
cyPoly34 = [cyTop3, cyBottom3, cyBottom4, cyTop4]
cyPoly45 = [cyTop4, cyBottom4, cyBottom5, cyTop5]
cyPoly56 = [cyTop5, cyBottom5, cyBottom6, cyTop6]
cyPoly67 = [cyTop6, cyBottom6, cyBottom7, cyTop7]
cyPoly78 = [cyTop7, cyBottom7, cyBottom8, cyTop8]
cyPoly81 = [cyTop8, cyBottom8, cyBottom1, cyTop1]
# Definition of the objects
Pyramid = [pybottompoly, pyfrontpoly, pyrightpoly, pybackpoly, pyleftpoly]
Cube = [sqBottomPoly, sqFrontPoly, sqRightPoly, sqBackPoly, sqLeftPoly, sqTopPoly]
Pyramid1 = [py1bottompoly, py1frontpoly, py1rightpoly, py1backpoly, py1leftpoly]
Cylinder = [cyPoly12, cyPoly23, cyPoly34, cyPoly45, cyPoly56, cyPoly67, cyPoly78, cyPoly81]
# Definition of the Pyramids'  and Cubes' underlying point clouds.  No structure, just the points.
# Also contains point clouds for default points
PyramidPointCloud = [pyapex, pybase1, pybase2, pybase3, pybase4, pyCenter]
CubePointCloud = [sqBase1, sqBase2, sqBase3, sqBase4, sqBase5, sqBase6, sqBase7, sqBase8, sqCenter]
DefaultPyramidCloud = [pydApex, pydBase1, pydBase2, pydBase3, pydBase4, pydCenter]
DefaultCubeCloud = [sqDBase1, sqDBase2, sqDBase3,sqDBase4, sqDBase5, sqDBase6, sqDBase7, sqDBase8, sqDCenter]
PyramidPointCloud1 = [py1apex, py1base1, py1base2, py1base3, py1base4, py1Center]
DefaultPyramidCloud1 = [py1dApex, py1dBase1, py1dBase2, py1dBase3, py1dBase4, py1dCenter]
CylinderPointCloud = [cyTop1, cyTop2, cyTop3, cyTop4, cyTop5, cyTop6, cyTop7, cyTop8,
                      cyBottom1, cyBottom2, cyBottom3, cyBottom4, cyBottom5, cyBottom6, cyBottom7, cyBottom8, cyCenter]
DefaultCylinderCloud = [cydTop1, cydTop2, cydTop3, cydTop4, cydTop5, cydTop6, cydTop7, cydTop8,
                      cydBottom1, cydBottom2, cydBottom3, cydBottom4, cydBottom5, cydBottom6, cydBottom7, cydBottom8, cydCenter]

#Use a dictionary to keep track of the PointCloud being used
PointCloud = dict([(0,[PyramidPointCloud, DefaultPyramidCloud]), (1,[CubePointCloud, DefaultCubeCloud]),
                   (2,[PyramidPointCloud1, DefaultPyramidCloud1]), (3,[CylinderPointCloud, DefaultCylinderCloud])])
#Start the scene with the defined objects

#Scene = [Pyramid, Cube, Pyramid1, Cylinder]
#Scene = [Pyramid]
#Scene = [Cube]
Scene = [Cylinder]
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
        rotate = [[math.cos(math.radians(degrees)), math.sin(math.radians(degrees)), 0, 0],
                   [-1 * math.sin(math.radians(degrees)), math.cos(math.radians(degrees)), 0, 0],
                   [0, 0, 1, 0],
                   [0, 0, 0, 1]]
        #make a temporary point for rotation
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])):
            object[index][i] = matrixMultiplication(temp, rotate)[i]
        
            
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
        rotate = [[math.cos(math.radians(degrees)), 0, -1 * math.sin(math.radians(degrees)), 0],
                   [0, 1, 0, 0],
                   [math.sin(math.radians(degrees)), 0, math.cos(math.radians(degrees)), 0],
                   [0, 0, 0, 1]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateO)[i]
        #Use rotate formula for y rotation
        #make a temporary point for rotation
        temp = [object[index][0], object[index][1], object[index][2], object[index][3]]
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(temp, rotate)[i]
        
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
        rotate = [[1, 0, 0, 0],
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
            object[index][i] = matrixMultiplication(temp, rotate)[i]
        
        for i in range(0, len(object[index])): #every coordinate in each point
            object[index][i] = matrixMultiplication(object[index], translateB)[i]
        


#The function will draw every object in the scene by repeatedly calling drawObject on each object in the scene
def drawScene(scene):
    global shape
    #the zbuffer should be in the scene
    #This should be done in a scene
    #create a depth buffer using an array of zbuffers
    zbuffer = []
    for i in range(CanvasWidth):
        row = []
        for j in range(CanvasWidth):
            row.append(math.inf)
        zbuffer.append(row)
    for index in range(len(scene)):
        if(index == shape):
            color = "green"
        else:
            color = "blue"
        drawObject(scene[index], color, zbuffer)
        
# The function will draw an object by repeatedly calling drawPoly on each polygon in the object
def drawObject(object, lcolor, zbuffer): #Overload the function to switch the point clouds when selecting shapes
    for poly in object: #draw a polygon for each polygon in the object array
        drawPoly(poly,lcolor, zbuffer)

# This function will draw a polygon by repeatedly callying drawLine on each pair of points
# making up the object.  Remember to draw a line between the last point and the first.
def drawPoly(poly, lcolor, zbuffer):
    #include toggle for back face culling
    global backFace
    global fill
    global lighting
    #predefined ambient intensity
    #Ambient intensity should be low because it represents the darkest part of the shade
    Ia = [0.2, 0.2, 0.2]
    #I get to define kd and kg and n values (but n should be big enough for noticeable shine)
    kd = [180, 150, 0]
    kg = [200, 200, 200]
    #n shininess
    n = 160
    #this is where decide whether to draw a poly or not
    #x, y, z are in poly
    #A, B, C come from the first 3 points
    A = ((poly[1][1] - poly[0][1]) * (poly[2][2] - poly[0][2]) -
         (poly[2][1] - poly[0][1]) * (poly[1][2] - poly[0][2]))
    B = -1 * ((poly[1][0] - poly[0][0]) * (poly[2][2] - poly[0][2]) -
         (poly[2][0] - poly[0][0]) * (poly[1][2] - poly[0][2]))
    C = ((poly[1][0] - poly[0][0]) * (poly[2][1] - poly[0][1]) -
         (poly[2][0] - poly[0][0]) * (poly[1][1] - poly[0][1]))
    #the scalar D
    D = A * poly[0][0] + B * poly[0][1] + C * poly[0][2]
        #the current point cloud should hold all of the vertices
    for vertex in currCloud:
        sumx = 0
        sumy = 0
        sumz = 0
        for polygon in currObject:
            if polygon.__contains__(vertex):
                sumx += A
                sumy += B
                sumz += C
        magnitude = math.sqrt(sumx ** 2 + sumy ** 2 + sumz ** 2)
        if(magnitude):
            vertNormx = sumx/magnitude
            vertNormy = sumy/magnitude
            vertNormz = sumz/magnitude
        else:
            vertNormx = 0
            vertNormy = 0
            vertNormz = 0
    #Create the edge table
    edgeTable = []
    for i in range(0, len(poly) - 1): #draw a line between the first points
        #test the the visibility of all points before drawing them
        #                   Ax                By               Cz              d
        visibility_result = ( 0) + ( 0) + (int(C) * -1 * d) - int(D) #(using 0,0,-1) as center of projection
        # the result is above 0 the plane is visible
        if(visibility_result > 0 or not backFace):
            drawLine(poly[i], poly[i+1], edgeTable, lcolor) #calculate edges where the line is drawn and add them to the table
        else:
            continue
    #this always happens so we gotta make a check for it too
    visibility_result0 = int(C) * -1 * d - int(D)
    visibility_result1 = int(C) * -1 * d - int(D)
    if(visibility_result0 > 0 and visibility_result1 > 0 or not backFace):
        drawLine(poly[-1], poly[0],edgeTable, lcolor)  #draw a line between the last and first
    #time to fill the polygon now that the edge table is finished
    #find yMin and yMax
    #this section only runs if filling is turned on and there are edges drawn
    if(fill and edgeTable != []):
            #sort by Ystart
        for i in range(1,len(edgeTable)):
            for j in range(i, 0, -1):
                if(edgeTable[j-1][1] < edgeTable[j][1]):
                    break
                edgeTable[j - 1], edgeTable[j] = edgeTable[j], edgeTable[j - 1]
        yMin = edgeTable[0][1]
        yMax = edgeTable[0][0]
        for edge in edgeTable:
            if(edge[0] > yMax):
                yMax = edge[0]
    #lets find xmin and xmax
        xMin = edgeTable[0][3]
        xMax = edgeTable[0][3]
        for edge in edgeTable:
            if(edge[3] > xMax):
                xMax = edge[3]
            if(edge[3] < xMin):
                xMin = edge[3]
    #find the active edges
    #The first 2 edges should be the firs 2 in the sorted table
    #first edge is the one with the smaller dx [2]
                    
        if(edgeTable[0][2] <= edgeTable[1][2]):
            firstEdge = edgeTable[0]
            secondEdge = edgeTable[1]
        else:
            firstEdge = edgeTable[1]
            secondEdge = edgeTable[0]
    #draw a 1 pixel rectangle between the 2 Ys
        x1 = firstEdge[3]
        x2 = secondEdge[3]
        #need to keep track of what edge table is next
        nextEdge = 2
        #Set the initial values of ZA and ZB outside of the loop
        #Technically zA0 and zB0
        zA = firstEdge[5]
        zB = secondEdge[5]
        #calculate the change once per edge since it's constant per edge
        zChangeA = (firstEdge[4] - firstEdge[5])/(firstEdge[0] - firstEdge[1])
        zChangeB = (secondEdge[4] - secondEdge[5])/(secondEdge[0] - secondEdge[1])
        for y in range(int(yMin), int(yMax)):
            #replace the edges if the y value becomes greater than the end of the edge
        #but only if these are not the last 2 edges
            #changing edges also means changing z values
            if(y > firstEdge[0]):
                if(nextEdge < (len(edgeTable))):
                    
                    firstEdge = edgeTable[nextEdge]
                    x1 = firstEdge[3]
                    zA = firstEdge[5]
                    zChangeA = (firstEdge[4] - firstEdge[5])/(firstEdge[0] - firstEdge[1])
                    nextEdge += 1
                else:
                    firstEdge = edgeTable[0]
                    zA = firstEdge[5]
                    zChangeA = (firstEdge[4] - firstEdge[5])/(firstEdge[0] - firstEdge[1])
                    x1 = firstEdge[3]
            if(y > secondEdge[0]):
                if(nextEdge < (len(edgeTable))):
                    secondEdge = edgeTable[nextEdge]
                    x2 = secondEdge[3]
                    zB = secondEdge[5]
                    zChangeB = (secondEdge[4] - secondEdge[5])/(secondEdge[0] - secondEdge[1])
                    nextEdge += 1
                else:
                    secondEdge = edgeTable[0]
                    zB = secondEdge[5]
                    zChangeB = (secondEdge[4] - secondEdge[5])/(secondEdge[0] - secondEdge[1])
                    x2 = secondEdge[3]      
            #let xMin is 1 and xMax is 0
            #how about distance to xmax/ total distance of xmax to xmin
            #(xmax - x1)/(xmax - xmin)
 ############Intensity1 and Intensity2 need to be determined before here#################################
            #use the first edge to find zA1 and the second edge for zB1
            zA += zChangeA
            zB += zChangeB
            #print pixels from one edge to another
            #If the first edge is on the left, go from first to second edge x-wise
            step = 1
            if(x1 > x2):
                step = -1
                #change the value of color using fx
            #definition of a single light source
            #It is a (1, 1, -1) vector at a 45 degree angle over viewer's right shoulder (0, 0, -d)
            #the normal of the lighting vector
            lightLoc = convertToDisplayCoordinates(project([1, 1, (1 + d)]))
            normalL = [1, 1, -1]
            
            #definition of a light source which is now white
            lightColor = [255, 255,255]
            #initialize zAB outside the loop
            zAB = zA
            if(x1 != x2):
                zChangeAB = (zB - zA)/(step * (x1 - x2)) #use step to make sure its the correct x values
            else:
                zChangeAB = 0
            for x in range(int(x1), int(x2), step):
                zAB += zChangeAB
                #this is actually the distance from the light source
                Ip = [1 - (abs(x1-lightLoc[0])/lightLoc[0]), 1 - (abs(x1-lightLoc[0])/lightLoc[0]), 1 - (abs(x1-lightLoc[0])/lightLoc[0])]
                #I have the x, y, and z values, so I just need to normalize them
                lengthN = (math.sqrt(x ** 2 + y ** 2 + zAB ** 2))
                normalN = [x/lengthN, y/lengthN, zAB/lengthN]
                #The dot product
                NL = normalL[0] * normalN[0] + normalL[1] * normalN[1] + normalL[2] * normalN[2]
                #continue if the z value of the current point is less than z value drawn at the same spot
                #Also continue if z-buffer is off
                #update the array if there isnt one or the current point is less than the z value
                if(buffer):
                    if(zbuffer[x][y] > zAB):
                        zbuffer[x][y] = zAB
                    else:
                        continue #don't do anything this iteration
                else: #set the zbuffer to default so it can toggle correctly
                    zbuffer[x][y] = math.inf
                #convert numbers into string values between 0 and 255 and put them in temporary values
                color = []
                if(NL > 0):
                    #R = N - L/(2*NL)
                    R = [normalN[0] - (normalL[0]/(2 * NL)), normalN[1] - (normalL[1]/(2 * NL)), normalN[2] - (normalL[2] /(2 * NL))]
                elif(NL < 0):
                    #R = -N + L/(2*NL)
                    R = [ -1 * normalN[0] + (normalN[0]/(2 * NL)), -1 * normalN[1] + (normalL[1]/(2 * NL)), -1 * normalN[2] + (normalL[2] /(2 * NL))]
                else:
                    R = [-1 * normalL[0], -1 * normalL[1], -1 * normalL[2]]
                lengthR = math.sqrt(R[0] ** 2 + R[1] ** 2 + R[2] ** 2)
                normalR = [R[0]/lengthR, R[1]/lengthR, R[2]/lengthR]
                #V is our view point (0, 0, -d)
                V = [0, 0, -1 * d]
                lengthV = math.sqrt(V[0] ** 2 +  V[1] ** 2 + V[2] ** 2)
                normalV = [V[0]/lengthV, V[1]/lengthV, V[2]/lengthV]
                #Now the dot products of R and V
                RV = normalR[0] * normalV[0] + normalR[1] * normalV[1] + normalR[2] * normalV[2]
                #n shininess
                n = 5
                #we get z value from zbuffer[x][y], we got other points from x and y
                for i in range(3):
                    #ambient diffuse and lamberg shading
                    I = kd[i] * Ia[i]
                    #point diffuse and gouraud shading
                    if(diffuse):
                        #add Ip * kd * (N dot L)/d
                        I += Ip[i] * kd[i] * NL
                        
                    #specular and phong shading
                    if(specular):
                    #add Ip * kg * (R dot V)
                        RV = abs(RV)
                        I += Ip[i] * kg[i] * (RV ** n)
                    if(I > 255):
                        I = 255
                    if(I < 16):
                        color.append("0" + str(hex(int(I)))[2:])
                    else:
                        color.append(str(hex(int(I)))[2:])
                        #color.append(fcolor[i])
                pixel = w.create_rectangle(x, y, x + 1, y + 1, outline="#" +color[0] + color[1] + color[2])
        #increment the edges' x value wit the dx value
            x1 -= firstEdge[2]
            x2 -= secondEdge[2]
        #replace the edges if the y value becomes greater than the end of the edge
        #but only if these are not the last 2 edges
            if(y > firstEdge[0]):
                if(i < (len(edgeTable) - 1)):
                    i += 1
                    firstEdge = edgeTable[i]
                    x1 = firstEdge[3]
                else:
                    firstEdge = edgeTable[0]
                    x1 = firstEdge[3]
            if(y > secondEdge[0]):
                if(i < (len(edgeTable) - 2)):
                    secondEdge = edgeTable[i + 2]
                    x2 = secondEdge[3]
                else:
                    secondEdge = edgeTable[0]
                    x2 = secondEdge[3]
               

# Project the 3D endpoints to 2D point using a perspective projection implemented in 'project'
# Convert the projected endpoints to display coordinates via a call to 'convertToDisplayCoordinates'
# draw the actual line using the built-in create_line method
def drawLine(start,end,edgeTable, color):
    #project the endpoints
    global edges
    projectedS = project(start)
    projectedE = project(end)
    
    #convert projected points to display coordinates
    startdisplay = convertToDisplayCoordinates(projectedS)
    enddisplay = convertToDisplayCoordinates(projectedE)
    if(edges):
        w.create_line(startdisplay[0], startdisplay[1], enddisplay[0], enddisplay[1], fill=color)
    #Edges start from the the point with the lower y to the point with the higher y
    if (math.trunc(startdisplay[1]) < math.trunc(enddisplay[1])):
        xEnd = enddisplay[0]
        xStart = startdisplay[0]
        #need the projected z value for z-buffer
        zEnd = projectedE[2]
        zStart = projectedS[2]
        #y values have to be truncated
        yEnd = math.trunc(enddisplay[1]) + 0.5
        yStart = math.trunc(startdisplay[1]) + 0.5
        dx =  -1 * (xEnd - xStart)/ (yEnd - yStart)
        #add the z values of the end points to the edge table
        edge = [yEnd, yStart, dx, xStart, zEnd, zStart]
        edgeTable.append(edge)
    elif (math.trunc(startdisplay[1]) > math.trunc(enddisplay[1])):
        xEnd = startdisplay[0]
        xStart = enddisplay[0]
        #need the projected z value for z-buffer
        zStart = projectedE[2]
        zEnd = projectedS[2]
        yEnd = math.trunc(startdisplay[1]) + 0.5
        yStart = math.trunc(enddisplay[1]) + 0.5
        dx =  -1 * (xEnd - xStart)/ (yEnd - yStart)
        edge = [yEnd, yStart, dx, xStart, zEnd, zStart]
        edgeTable.append(edge)
    
    else:
        #do nothing for horizontal lines
        pass

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
    
#Toggle back face culling on or off
def backface(_event=None):
    global backFace
    if(backFace):
        backFace = False
    else:
        backFace = True
    #update scene
    w.delete(ALL)
    drawScene(Scene)

#Toggle poly fill on or off
def filling(_event=None):
    global fillPoint
    global fill
    global edges
    fillPoint += 1
    if(fillPoint > 2):
        fillPoint = 0
    if(fillPoint == 1):
        fill = True
    elif(fillPoint == 2):
        edges = False
    else:
        fill = False
        edges = True
    #update scene
    w.delete(ALL)
    drawScene(Scene)
    
#Toggle on or off z-buffer
def zBuffer(_event=None):
    global buffer
    if(buffer):
        buffer = False
    else:
        buffer = True
    #update Scene
    w.delete(ALL)
    drawScene(Scene)

#Change the lighting
def light(_event=None):
    global lighting
    global diffuse
    global specular
    lighting += 1
    #make sure lighting never goes past 2
    if(lighting > 2):
        lighting = 0
    if(lighting == 1):
        diffuse = True
    elif(lighting == 2):
        specular = True
    else: #only zero, really
        diffuse = False
        specular = False
    #update scene
    w.delete(ALL)
    drawScene(Scene)

def shade(_event=None):
    global shading
    global gouraud
    global phong
    global lamberg
    shading += 1
    #make sure shading never goes past 2
    if(shading > 2):
        shading = 0
    if(shading == 1):
        gouraud = True
        lamberg = False
        phong = False
    elif(shading == 2):
        phong = True
        gouraud = False
        lamberg = False
    else:
        lamberg = True
        gouraud = False
        phong = False
    #update scene
    w.delete(ALL)
    drawScene(Scene)
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
#Use a currObject to keep track of what object is being selected
shape = 0 #this is a global variable for the current object in the scene being used
currObject = Scene[shape]
currCloud = PointCloud[3][0]
currDefCloud = PointCloud[3][1]
#toggle for backface
backFace = False
fillPoint = 0
#toggle for poly fill
fill = False
#toggle for edges being drawn
edges = True
#toggle for zbuffer
buffer = False
#Counter for which lighting to activate
lighting = 0
#toggle for point diffuse
diffuse = False
#toggle for point specular
specular = False
#toggle for lamberg shading
lamberg = False
#toggle for Gouraud
gouraud = False
#toggle for phong
phong = False
#counter for which shading to activate
shading = 0
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
root.bind('<b>', backface)
root.bind('<f>', filling)
root.bind('<z>', zBuffer)
root.bind('<l>', light)
root.bind('<s>', shade)

root.mainloop()