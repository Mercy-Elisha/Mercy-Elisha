#Functionb to calculate the volume of a cylinder
r = 56
h = 78

#Volume = pi* r * *r *h
volume = 3.142* r *r *h

#Display the volume
print ("The volume of the cylinder is:",volume, "cm^2")


#calculate the volume of a cylinder 
import math
#function to calculate the volume of a cylinder

def cylinder_volume(radius, height):
    #formular is pi*radius *radius *height
    volume = math.pi*radius*radius*height
    return volume

#input radius and height
radius= int(input("Enter the radius of the cylinder:"));
height =float(input("Enter the height of the cylinder:"));

#Calculate and display the volume
volume = cylinder_volume(radius , height) 
print(f"The Volume of the cylinder is:{volume }");


#calculate the volume of a sphere

def sphere_volume(radius):
    #formular = 4/3 *r *r
    volume = 4/3 *radius *radius
    return volume  

#input the value of radius
radius = int(input ("Enter the radius of the sphere:"));
print("The volume is" ,volume,);