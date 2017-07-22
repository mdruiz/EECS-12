# hw2.py
# Parabolic Trajectory
# Mario Ruiz ID:46301389

import math
def main():
    print ("This program calculates the height, velocity and velocity direction angle of Parabolic Trajectory of a ball.")
    velocity = eval(input("Enter the initial velocity from 100-200(m/s):"))
    angle = eval(input("Enter the initial angle, between 0 and 90:"))
    radians= math.pi*angle/180
    xVelocity = velocity*math.cos(radians)
    yVelocity = velocity*math.sin(radians)
    totalDistance=0
    ixVelocity= xVelocity
    windResistance = .5
    airTime= 2* (round(yVelocity)/10)
    print ("\t")
    time= 0
    Px= totalDistance
    print ("Time \t Angle \t \t \t Px \t \t \t Py")
    print ("0 \t ",angle, "\t \t \t 0 \t \t \t 0")
    y2Velocity= yVelocity
    for i in range (round(airTime)-1):
        time= time + 1
        Px= xVelocity + Px
        Py= yVelocity*(i+1)-5*(i+1)**2
        windResistance=3.9*windResistance*(1-windResistance)
        xVelocity= xVelocity- 0.1*windResistance*xVelocity
        y2Velocity = y2Velocity-10
        vAngle= math.sqrt(xVelocity**2+y2Velocity**2)
        Angle= math.asin(y2Velocity/vAngle)
        print(time,"\t",Angle*180/math.pi,"\t",Px,"\t",Py)
    xtra= 1-(math.ceil(airTime)-airTime)           
    totalDistance= Px+ xVelocity*round(xtra,1)
    print("\t")
    print("The total distance for the ball’s flight is", totalDistance) 

main()
