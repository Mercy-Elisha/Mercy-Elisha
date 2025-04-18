import math

#fucntion to calculate the volume of a cylinder
def cylinder_volume(radius,height):
    #formula: radius = pi *radius * radius * height
    volume = math.pi *radius* radius *height
    return volume
#input: Radius and Height
radius= float(input("Enter the radius of the cylinder:"))
height = float(input("Enter the height of the cylinder:"))

#calculate and display the volume
volume = cylinder_volume(radius , height)
print(f"The volume of the cylnder is: {volume: .2f}")
