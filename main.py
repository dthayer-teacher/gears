
import math

r1 = float(input("Enter r1 in meters: "))
r2 = float(input("Enter r2 in meters: "))

input_torque = float(input("What is the input torque in Newton-Meters: "))

bolt1 = float(input("Enter bolt hole pattern y-axis in meters: "))
bolt2 = float(input("Enter bolt hole pattern z-axis in meters: "))

# degree = 30
# rad = degree*(math.pi/180)
# print(math.sin(rad))
# calculations




mx = 0
convert = .0254
F=input_torque/r1
normalForce = F*math.tan(20*math.pi/180)

#momment sum of My
#input
Az = (normalForce*1.5*convert)/(1.5*convert+1*convert)
Bz = normalForce - Az
#sum of mz

Ay = (F*1.5*convert)/(1.5*convert+1*convert)
By = F - Ay
print("*******************************************")
print("Ay: ",round(Ay,4),"N")
print("By: ",round(By,4),"N")
print("Az: ",round(Az,4),"N")
print("Bz: ",round(Bz,4),"N")

#output


output_torque = F *r2
#sum moments in z
Cy = (F*1.5*convert)/(1.5*convert+1*convert)
Dy = F - Cy

Cz = (normalForce*1.5*convert)/(1.5*convert+1*convert)
Dz = normalForce - Cz
print("*******************************************")
print("Cy: ",round(Cy,4),"N")
print("Dy: ",round(Dy,4),"N")
print("Cz: ",round(Cz,4),"N")
print("Dz: ",round(Dz,4),"N")
print("*******************************************")
print("Output Torque: ",round(output_torque,4),"Nm")

#moment of x axis

# xaxis = (r2+r1)*192+(r2+r1)*128
xaxis = input_torque+output_torque

print("The moment about x-axis: ",round(xaxis,4),"Nm")
center_rotate = math.sqrt((bolt1/2)**2+(bolt2/2)**2)
# print("Center of rotation: ",center_rotate)

bolt_force = xaxis/(4*center_rotate)

print("Re = Rf = Rh = Ri = ",round(bolt_force,4),"N")