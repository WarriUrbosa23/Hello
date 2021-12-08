import math
#This is a program built by me, Mihir Pillay. What is it? An area calculator.
print ("This is an area calculator.")
choice = input ("What shape's area do you want to calcuate. Press 1 for circle, 2 for triangle, 3 for square, and 4 for rectangle. Type 'How did I do this?'")
if choice == "1":
    radius = input ("What is your radius? Type the number here.")#Diameter idea  
    circle_area = float(radius)*float(radius)*math.pi
    print ("Your circles area will be {} units" .format (circle_area))
#Part Two
if choice == "2":
    tri_base = input("What is your triangle's base?")
    tri_height = input("What is your triangle's height?")
    triangle_area = float(tri_base)*float(tri_height)/2
    print ("A triangle like that would have an area of {} units" .format (triangle_area))
#Part Three
if choice == "3":
    SLW = input ("What is your legnth and height? If they aren't the same, go and do the rectangle thing.")
    Square_area = float(SLW)*float(SLW)
    print ("That square's area is {} units" .format (Square_area))
#Part Four
if choice == "4":
    rectangle_length = input ("What is your rectangle's length?")
    rectangle_height = input ("What is your rectangle's height?")
    rectangle_area = float(rectangle_height)*float(rectangle_length)
    print ("That rectangle's area is {}" .format (rectangle_area))
#Extra!!!!!!!!!!!!!!!!!!!!
if choice == "How did I do this?":
    print("I did it using Python 3.8.2. It's super easy and fun!")
else:
    print ("Nothing to see here.")
