import turtle
print('Triangle Validity\n')


x1 = float(input('Enter the x value of point 1: '))
while x1 < 0:
    x1 = float(input('Por favor enter a non-negative number: '))

y1 = float(input('Enter the y value for point 1: '))
while y1 < 0:
    y1 = float(input('Por favor enter a non-negative number: '))
print()

x2 = float(input('Enter the x value for point 2: '))
while x2 < 0:
    x2 = float(input('Por favor enter a non-negative number: '))

y2 = float(input('Enter the y value for point 2: '))
while y2 < 0:
    y2 = float(input('Por favor enter a non-negative number: '))
print()

x3 = float(input('Enter the x value for point 3: '))
while x3 < 0:
    x3 = float(input('Por favor enter a non-negative number: '))

y3 = float(input('Enter the y value for point 3: '))
while y3 < 0:
    y3 = float(input('Por favor enter a non-negative number: '))
print()

print('Here are the lengths of each side of the triangle.')
side1 = ((x1-x2)**2 + (y1-y2)**2)**0.5
print('Side 1:', format(side1, '.2f'))
side2 = ((x2-x3)**2 + (y2-y3)**2)**0.5
print('Side 2:', format(side2, '.2f'))
side3 = ((x1-x3)**2 + (y1-y3)**2)**0.5
print('Side 3:', format(side3, '.2f'),'\n') 

if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    print('This is a valid triangle.')
    if side1 == side2 == side3:
        print('It is equilateral.')
    elif side1 == side2 or side1 == side3 or side2 == side3:
        print('It is isosceles.')
    else:
        print('It is scalene.')
    
    max_size = max([x1, x2, x3, y1, y2, y3]) #This gives us the largest number to scale our drawing board
   
    draw_triangle = input('Would you like to draw the triangle? (yes/no): ')
    
    if draw_triangle == 'yes':
        window = turtle.Screen()
        window.setup(width=640, height=640)
        window.setworldcoordinates(0, 0, 2 * max_size, 2 * max_size) 
        if side1 == side2 == side3:
            turtle.pencolor("green")
        elif side1 == side2 or side1 == side3 or side2 == side3:
            turtle.pencolor("blue")
        else:
            turtle.pencolor("red")
   
        turtle.penup()
        turtle.goto(x1,y1)
        turtle.pendown()
        turtle.goto(x2,y2)
        turtle.goto(x3,y3)
        turtle.goto(x1,y1)
        turtle.penup()
else:
    print('This is not a valid triangle.')









