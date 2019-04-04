#Elijah Jefferson
#02/14/2019
#Simulate reflective spheres using ray tracing
#Treat colors as percentages and calculate the actual color at the end
import math
from tkinter import *

CanvasWidth = 1200
CanvasHeight = 1200
d = 800
#I'll initialize spheres with a center and radius instead of cubes and pyramids with vertices
sphere1 = [150, 200, 500, 100, [120, 180, 0]]
sphere2 = [500, 100, 200, 150, [200, 100, 100]]
Scene = [sphere1, sphere2]

#checks if a ray crosses the checkerboard
#Will return t and the intersect values along with the flag
def checkerboard_intersection(xs, ys, zs, ray_x, ray_y, ray_z):
    #Use globals instead of pointers
    global t
    global intersect_x
    global intersect_y
    global intersect_z
    #get the normal of the plane
    a = 0
    b = 1
    c = 0
    #get the point on the plane
    x1 = 0
    y1 = -500
    z1 = 0
    #computer intersection of ray with plane
    denom = a * ray_x + b * ray_y + c *ray_z
    if (math.fabs(denom) <= 0.001):
        return 0 #this means ray is parallel to plane
    else:
        D = a * x1 + b * y1 + c * z1
        t_object = -1 * (a * xs + b * ys + c * zs - D)/ denom
        x = xs + ray_x * t_object
        y = ys + ray_y * t_object
        z = zs + ray_z * t_object
        if((z < 0.0) or (z > 8000) or (t_object < 0.0)):
            return 0 #no visible intersection
        elif (t < t_object):
            return 0 #another object is nearer
        else:
            t = t_object
            intersect_x = x
            intersect_y = y
            intersect_z = z
            return 1

#computes the intensiy of the checkerboard
#will return the rgb values
def checkerboard_point_intensity(level, ray_x, ray_y, ray_z):
    #switch pointers for global variables
    global ir
    global ig
    global ib
    global intersect_x
    global intersect_y
    global intersect_z
    x = intersect_x
    y = intersect_y
    z = intersect_z

    magnitude = math.sqrt(ray_x ** 2 + ray_y ** 2 + ray_z ** 2)
    ray_x_norm = 1/magnitude
    ray_y_norm = 1/magnitude
    ray_z_norm = 1/magnitude

    magnitude = math.sqrt(1 ** 2 + 1 ** 2 + 1 ** 2)
    if(magnitude == 0):
        nx_norm = 0
        ny_norm = 0
        nz_norm = 0
    else:
        nx_norm = 1/magnitude
        ny_norm = 1/magnitude
        nz_norm = 1/magnitude

    #calculate reflection vector
    cosine_phi = (-1*ray_x_norm * nx_norm) + (-1*ray_y_norm * ny_norm) + (-1*ray_z_norm * nz_norm)
    if(cosine_phi > 0):
        rx = nx_norm - (-1*ray_x_norm) / (2 * cosine_phi)
        ry = ny_norm - (-1*ray_y_norm) / (2 * cosine_phi)
        rz = nz_norm - (-1*ray_z_norm) / (2 * cosine_phi)
    if(cosine_phi == 0):
        rx = ray_x_norm
        ry = ray_y_norm
        rz = ray_z_norm
    if(cosine_phi < 0):
        rx = -1*nx_norm + (-1*ray_x_norm) / (2 * cosine_phi)
        ry = -1*ny_norm + (-1*ray_y_norm) / (2 * cosine_phi)
        rz = -1*nz_norm + (-1*ray_z_norm) / (2 * cosine_phi)
    #trace the reflection ray
    trace_ray(0, level - 1, x, y, z, rx, ry, rz)

    #compute color at intersection
    if(x >= 0.0):
        color_flag = True
    else:
        color_flag = False
    if(abs(x % 1000) > 500):
        color_flag = not color_flag
    if(abs(z % 1000) > 500):
        color_flag = not color_flag
    if(color_flag):
        ir = 255
        ig = 0
        ib = 0
        #red
    else:
        ir = 255
        ig = 255
        ib = 255
        #white

#calculates the intersection of a sphere
#Will return t and the intersect values
def sphere_intersection(xs, ys, zs, ray_x, ray_y, ray_z, sphere):
    #Use globals instead of pointers
    global t
    global intersect_x
    global intersect_y
    global intersect_z
    global obj_normal_x
    global obj_normal_y
    global obj_normal_z
    #The center of the sphere
    l = sphere[0]
    m = sphere[1]
    n = sphere[2]
    #radius of the sphere
    r = sphere[3]
    #compute the intersection of ray with spheres
    asphere = ray_x ** 2 + ray_y ** 2 + ray_z ** 2
    bsphere = 2 * ray_x * (xs - l) + 2 * ray_y * (ys - m) + 2 * ray_z * (zs - n)
    csphere = l ** 2 + m ** 2 + n ** 2 + xs ** 2 + ys ** 2 + zs ** 2 + 2 * ((-1 * l) * xs - m * ys -
    n * zs) - r ** 2
    disc = bsphere ** 2 - 4 * asphere * csphere
    if(disc < 0):
        return 0
    else:
        ts1 = (-1 * bsphere + math.sqrt(disc)) / (2 * asphere)
        ts2 = (-1 * bsphere - math.sqrt(disc)) / (2 * asphere)
        if(ts1 >= ts2):
            tsphere = ts2
        else:
            tsphere = ts1
        if(t < tsphere):
            return 0 #another object is closer
        elif(tsphere <= 0.0):
            return 0 #no visible intersection
        else:
            t = tsphere
            intersect_x = xs + ray_x * tsphere
            intersect_y = ys + ray_y * tsphere
            intersect_z = zs + ray_z * tsphere
            obj_normal_x = intersect_x - l
            obj_normal_y = intersect_y - m
            obj_normal_z = intersect_z - n
            return 1

def sphere_point_intensity(level, ray_x, ray_y, ray_z, color):
    #switch pointers for globals
    global ir
    global ig
    global ib
    global t
    global intersect_x
    global intersect_y
    global intersect_z
    global obj_normal_x
    global obj_normal_y
    global obj_normal_z
    x = intersect_x
    y = intersect_y
    z = intersect_z
    nx = obj_normal_x
    ny = obj_normal_y
    nz = obj_normal_z
    #normalize ray vector  and surface normal vector
    magnitude = math.sqrt(ray_x ** 2 + ray_y ** 2 + ray_z ** 2)
    ray_x_norm = nx/magnitude
    ray_y_norm = ny/magnitude
    ray_z_norm = nz/magnitude

    magnitude = math.sqrt(nx ** 2 + ny ** 2 + nz ** 2)
    if(magnitude == 0):
        nx_norm = 0
        ny_norm = 0
        nz_norm = 0
    else:
        nx_norm = nx/magnitude
        ny_norm = ny/magnitude
        nz_norm = nz/magnitude

    #calculate reflection vector
    cosine_phi = (-1*ray_x_norm * nx_norm) + (-1*ray_y_norm * ny_norm) + (-1*ray_z_norm * nz_norm)
    if(cosine_phi > 0):
        rx = nx_norm - (-1*ray_x_norm) / (2 * cosine_phi)
        ry = ny_norm - (-1*ray_y_norm) / (2 * cosine_phi)
        rz = nz_norm - (-1*ray_z_norm) / (2 * cosine_phi)
    if(cosine_phi == 0):
        rx = ray_x_norm
        ry = ray_y_norm
        rz = ray_z_norm
    if(cosine_phi < 0):
        rx = -1*nx_norm + (-1*ray_x_norm) / (2 * cosine_phi)
        ry = -1*ny_norm + (-1*ray_y_norm) / (2 * cosine_phi)
        rz = -1*nz_norm + (-1*ray_z_norm) / (2 * cosine_phi)
    #trace the reflection ray
    trace_ray(0, level - 1, x, y, z, -1*rx, -1*ry, -1*rz)
    #add affect of locol color and phong illumination
    #Ip * ks * (R * V)^n
    ks = [50, 50, 50]
    kd = [200, 200, 200]
    normalL = [1, 1, -1]
    Ia = [0.1, 0.1, 0.1]
    #Ip is distance from light source
    lightLoc = convertToDisplayCoordinates(project([1, 1, 801]))
    Ip = [.7 * ir + .3 * color[0], .7 * ig + .3 * color[1], .7 * ib + .3 * color[2]]
    #n_normals are the normal values
    NL = normalL[0] * nx_norm + normalL[1] * ny_norm + normalL[2] * nz_norm
    R = [rx, ry, rz]
    lengthR = math.sqrt(R[0] ** 2 + R[1] ** 2 + R[2] ** 2)
    normalR = [R[0]/lengthR, R[1]/lengthR, R[2]/lengthR]
    V = [0, 0, -800]
    lengthV = math.sqrt(V[0] ** 2 + V[1] ** 2 + V[2] ** 2)
    normalV = [V[0]/lengthV, V[1]/lengthV, V[2]/lengthV]
    RV = normalR[0] * normalV[0] + normalR[1] * normalV[1] + normalR[2] * normalV[2]
    #n is shininess
    n = 120
    #           +ambient        +diffuse                 +specular
    ir = kd[0] * Ia[0] +  Ip[0] * kd[0] * NL/d
    ig = kd[1] * Ia[1] +  Ip[1] * kd[1] * NL/d 
    ib = kd[2] * Ia[2] +  Ip[2] * kd[2] * NL/d 
    #ir = Ip[0]
    #ig = Ip[1]
    #ib = Ip[2]

def put_pixel(x, y, ir, ig, ib):
    i = []
    if(ir > 255):
        ir = 255
    if(ir < 0):
        ir = 0
    if(ir < 16):
        i.append("0" + str(hex(int(ir)))[2:])
    else:
        i.append(str(hex(int(ir)))[2:])
    if(ig > 255):
        ig = 255
    if(ig < 0):
        ig = 0
    if(ig < 16):
        i.append("0" + str(hex(int(ig)))[2:])
    else:
        i.append(str(hex(int(ig)))[2:])
    if(ib > 255):
        ib = 255
    if(ib < 0):
        ib = 0
    if(ib < 16):
        i.append("0" + str(hex(int(ib)))[2:])
    else:
        i.append(str(hex(int(ib)))[2:])
    w.create_rectangle(x, y, x + 1, y + 1, outline="#" + i[0] + i[1] + i[2])

#return the colors
def trace_ray(flag, level, xs, ys, zs, ray_i, ray_j, ray_k):
    global t
    global intersect_x
    global intersect_y
    global intersect_z
    global obj_normal_x
    global obj_normal_y
    global obj_normal_z
    global ir
    global ig
    global ib
    if(level == 0): #maximum depth, which means the color is black
        ir = 0
        ig = 0
        ib = 0
    else:
        #Check for intersection of ray with objects
        #and set rgb values to the right objects
        #set the distance of the closest object to a large number
        t = math.inf
        #default case is no object intersects the ray
        object_code = -1
        if(checkerboard_intersection(xs, ys, zs, ray_i, ray_j, ray_k)):
            object_code = 0
            if(flag):
                print("checkerboard")
        for i in range(len(Scene)):
            if(sphere_intersection(xs, ys, zs, ray_i, ray_j, ray_k, Scene[i])):
                object_code = i + 1 #there's already a code 0
        #switch cases aren't that simple in python, so I'm just gonna use if else
        #calculate intensity on objects hit by the ray
        if(object_code == 0):
            checkerboard_point_intensity(level, ray_i, ray_j, ray_k)
        elif(object_code >= 1):
            sphere_point_intensity(level, ray_i, ray_j, ray_k, Scene[object_code - 1][-1])
        else:
            ir = 150
            ig = 150
            ib = 255

#draws the scene
def render():
    depth = 5
    global ir
    global ig
    global ib
    #center of projection
    xs = 0
    ys = 0
    zs = -800
    #paint screen
    for pixel_x in range(1, 1200):
        screen_x = pixel_x - 600
        for pixel_y in range(1, 1200):
            screen_y = 600 - pixel_y
            #compute ray vector from center of projection to pixel
            ray_i = screen_x - xs
            ray_j = screen_y - ys
            ray_k = 0 - zs
            #trace the ray through the environment to get a pixel color
            trace_ray(0, depth, xs, ys, zs, float(ray_i), float(ray_j), float(ray_k))
            put_pixel(pixel_x, pixel_y, ir, ig, ib)
            w.update_idletasks()

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

    
root = Tk()
outerframe = Frame(root)
outerframe.pack()

w = Canvas(outerframe, width=CanvasWidth, height=CanvasHeight)
w.create_window(0,0, height = 600, width = 600)
w.delete(ALL)
w.pack()

controlpanel = Frame(outerframe)
controlpanel.pack()
t = 0
intersect_x = 0
intersect_y = 0
intersect_z = 0
obj_normal_z = 0
obj_normal_x = 0
obj_normal_y = 0
ir = 255
ig = 255
ib = 255
render()

root.mainloop()
