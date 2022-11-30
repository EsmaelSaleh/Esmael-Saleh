# Print multiple shapes

def DrawPyramid(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()


def DrawRectangle(height):
    for i in range(height):
        for j in range(height):
            print("* ", end="")
        print()


def DrawSquare(height):
    for i in range(height):
        for j in range(i+1):
            print("* ", end="")
        print()


def DrawDiamond(height):
    for i in range(height):
        for j in range(height-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("* ", end="")
        print()
    for i in range(height-1):
        for j in range(i+1):
            print(" ", end="")
        for j in range(height-i-1):
            print("* ", end="")
        print()


def DrawCircle(diameter):
    row = diameter
    col = diameter
    for i in range(0, row):
        for j in range(0, col):
            if((j == 0 or j == col-1) and (i != 0 and i != row-1)):
                # end='' so that print statement should not change the line.
                print('*', end='')
            elif(((i == 0 or i == row-1) and (j > 0 and j < col-1))):
                print('*', end='')
            else:
                print(end=' ')  # to print the space.
        print()  # to change the line after iteration of inner loop.


shapes = []

while True:
    print("Choose the shape you want to draw")
    print("1. Pyramid")
    print("2. Square")
    print("3. Triangle")
    print("4. Diamond")
    print("5. Circle")
    print("6. Draw all shapes")
    choice = int(input())
    if choice == 1:
        print("Enter the height of the pyramid")
        len = int(input())
        shapes.append(("Pyramid", len))
    elif choice == 2:
        print("Enter the height of the square")
        len = int(input())
        shapes.append(("Square", len))
    elif choice == 3:
        print("Enter the height of the triangle")
        len = int(input())
        shapes.append(("Triangle", len))
    elif choice == 4:
        print("Enter the height of the diamond")
        len = int(input())
        shapes.append(("Diamond", len))
    elif choice == 5:
        print("Enter the Diameter of the circle")
        len = int(input())
        shapes.append(("Circle", len))
    elif choice == 6:
        break
    else:
        print("Invalid choice")

print()
# sort the shapes by their height
shapes.sort(key=lambda x: x[1])  # sort by height descending
print("Shapes sorted by height descending as:")
print(shapes)
print()

# print the shapes
for shape in shapes:
    print("Drawing a " + shape[0] + " with height " + str(shape[1]))
    if shape[0] == "Pyramid":
        DrawPyramid(shape[1])
    elif shape[0] == "Square":
        DrawRectangle(shape[1])
    elif shape[0] == "Triangle":
        DrawSquare(shape[1])
    elif shape[0] == "Diamond":
        DrawDiamond(shape[1])
    elif shape[0] == "Circle":
        DrawCircle(shape[1])
