X = 17 #Value of X

Y = 7 #Value of Y

Sum = X + Y #Sum of X and Y

print(Sum)#Display the sum of X and Y




#Function to calculate the area of a tringle

b  = 30
h = 40

#Area = 0.5 *b *h

Area = 0.5* 30 * 40
#display the output
print(f"The area of the trianle is: {Area} cm2")





#Function to calculate volume of a sphere
r  = 7

#Volume = 1.333 *pi *r *r *r
Volume = 1.333 *3.142 *r *r *r

#display the output
print("The volume of the sphere is:", Volume, "cm2")





print("hello world")


x = range(10)

num = 10
for n in x:
    print("*" * n)
    if n == 9:
        for n in x:
            
            print("*" * num )
            num = num - 1
