import math

# Asking the user to enter the lengths of all three sides of a triangle:

side1 = float(input("Please enter the length of side 1 of the triangle: "))
side2 = float(input("Please enter the length of side 1 of the triangle: "))
side3 = float(input("Please enter the length of side 1 of the triangle: "))

s = (side1 + side2 + side3) / 2

area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

print("The area of the triangle is: ",  area)

# Sorry, the program sometimes gives an error (depending on the values given by the user): 
# "math domain error". I have no idea why it occurs. 