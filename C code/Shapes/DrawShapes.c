#include <stdio.h>
#include <math.h>
#include <stdlib.h>
struct Shapes
{
    int NumberOfShape;
    char Name[30]; // Name of the shape (circle, square, rectangle, triangle), we can use it to print the name of the shape
};

// Mohamed
void DrawPyramid()
{
    int height, k;
    printf("Enter the Height of the Shape : ");
    scanf("%d", &height);
    if (height <= 5 && height > 3) // limit the height of the shape to be between 2 and 5
    {
        for (int i = 1; i <= height; ++i, k = 0) // loop for row of the shape
        {
            for (int space = 1; space <= height - i; ++space) // loop for column of the shape
            {
                printf("  ");
            }
            while (k != 2 * i - 1) // loop for number of stars in the shape
            {
                printf("* ");
                ++k;
            }
            printf("\n");
        }
    }
    else
    {
        printf("The Limit for Height is 5 to 2 ");
    }
}

// Mohamed
void DrawSquare()
{
    int height, i, j;
    printf("Enter the Height of the Shape : ");
    scanf("%d", &height);
    /* Iterate through N rows */
    for (i = 1; i <= height; i++)
    {
        /* Iterate over columns */
        for (j = 1; j <= height; j++)
        {
            /* Print star for each column */
            printf("*");
            printf("  "); // print spaces between each point
        }

        /* Move to the next line/row */
        printf("\n");
    }
}

// Ismael
void DrawTriangle()
{
    int height, i, j;
    printf("Enter the Height of the Shape : ");
    scanf("%d", &height);
    for (i = 1; i <= height; ++i) // loop for row of the shape
    {
        for (j = 1; j <= i; ++j) // loop for column of the shape
        {
            printf("* ");
        }
        printf("\n");
    }
}

// Ismael
void DrawCircle()
{
    int Diameter, rows, columns;
    printf("Enter the Diameter for Cricle : ");
    scanf("%d", &Diameter);
    int radius = Diameter / 2;                      // dealing with the half of the Diameter(Height)
    for (rows = 0; rows < (2 * radius + 1); rows++) // loop for row of circle
    {
        for (columns = 0; columns < (2 * radius + 1); columns++) // loop for column of circle
        {
            if (pow(rows - radius, 2) + pow(columns - radius, 2) <= pow(radius, 2) + 1) // check if the point is inside the circle
            {
                printf("*");
            }
            else // if point outside circle print space
            {
                printf(" ");
            }
            printf(" "); // print space between each point
        }
        printf("\n");
    }
}

int main()
{
    int NumberOption1;
    // Use Struct To Access ID FOR SHAPES
    struct Shapes Pyramid;
    struct Shapes Square;
    struct Shapes Trinagle;
    struct Shapes Circle;
    // intialize the ID for each shape
    Pyramid.NumberOfShape = 1;
    Square.NumberOfShape = 3;
    Circle.NumberOfShape = 2;
    Trinagle.NumberOfShape = 4;

    do // loop for the menu
    {
        printf(" 1.Pyramid     2.Circle     3.Square    4.Triangle  5.Exit ");
        printf("\n Enter the Number of the Shape : ");
        scanf("%d", &NumberOption1);
        if (NumberOption1 == Pyramid.NumberOfShape)
        {
            DrawPyramid();
        }
        else if (NumberOption1 == Square.NumberOfShape)
        {
            DrawSquare();
        }
        else if (NumberOption1 == Circle.NumberOfShape)
        {
            DrawCircle();
        }
        else if (NumberOption1 == Trinagle.NumberOfShape)
        {
            DrawTriangle();
        }
        else if (NumberOption1 == 5)
        {
            break;
        }
        else
        {
            printf(" Enter a Valid Number \n \n");
        }
    } while (1);

    return 0;
}