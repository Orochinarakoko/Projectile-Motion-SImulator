import math
import matplotlib.pyplot as plt
import vpython# import required libs

dt = 0.01 # small time increments for euler approximation

horiz_displacements = []
vert_displacements = []

#------------------------------------------------------------------------- Variables for an Idealised model , initialised to natural or optimal values.
try:
    g = float(input("Gravitational Field Strength: ")) 
except:
    g = 9.81

try:
    h = float(input("Initial height above ground level: "))
except:
    h = 0

try:
    ang = float(input("Angle of Projection :"))
except:
    ang = 45

u = float(input("Initial Speed : "))
#--------------------------------------------------------------------- Variables for a more complex model

try:
    density = float(input("Fluid Density : "))
except:
    density = 1.225

RefArea = float(input("Reference Area : "))
coefD = float(input("Coefficient of Drag : "))
mass = float(input("Mass : "))

uver = u * math.sin(math.radians(ang))

uhor = u*math.cos(math.radians(ang))

sVer = h
sHor = 0
vVer = uver
vHor = uhor


while sVer >= 0:
    vert_displacements.append(sVer)
    horiz_displacements.append(sHor)

    sVer = sVer + dt*vVer
    sHor = sHor + dt*vHor

    aver = -g + (coefD*density*(-vVer)*abs(vVer)*RefArea)/(2*mass)
    ahor = -(coefD*density*(vHor**2)*RefArea)/(2*mass)

    vVer = vVer + dt*aver
    vHor = vHor + dt*ahor

gradient = (vert_displacements[-1] - vert_displacements[-2]) / (horiz_displacements[-1] - horiz_displacements[-2])

xint = (-vert_displacements[-1])/(gradient) + horiz_displacements[-1]

horiz_displacements.append(xint)
vert_displacements.append(0)



body = vpython.sphere(pos = vpython.vector(0,h,0),make_trail = True)
ground = vpython.box(length = xint,width = xint/5 , height = 1,pos =vpython.vector(xint/2,-1,0))



for i in horiz_displacements:
    vpython.rate(1/dt)
    body.pos = vpython.vector(i,vert_displacements[horiz_displacements.index(i)],0)

figure1 = plt.figure(figsize=(10, 10))
plt.axhline(y=0, color="red")
plt.plot(horiz_displacements, vert_displacements)
plt.xlabel("Horizontal Displacement")
plt.ylabel("Vertical Displacement")
plt.show()

