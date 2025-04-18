try:
    result = 10/0
except ZeroDivisionError:
 print("Error: Division by zerois not allowed.")
else:
   print(result)

finally:
   print("Division done")



   #value error division of a number and alphabet#
X= int(input("pleaase enter value of x :"))
Y=int(input("pleaase enter value of y :"))
q=X/Y
print(q)


#file does not exist error
x = 10
y = 0
q= x/y