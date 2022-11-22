#include <stdio.h>
#include <stdlib.h>

int main()
{
    int secrectNumber = 5;
    int guess;
    int guessCount = 0;
    int guessLimit = 5;
    int outOfGuesses = 0;

    while (guess != secrectNumber && outOfGuesses == 0)
    {
        if (guessCount < guessLimit)
        {
            printf("Enter a number: ");
            scanf("%d", &guess);
            guessCount++;
        }
        else
        {
            outOfGuesses = 1;
        }
    }
    if (outOfGuesses == 1)
    {
        printf("out of Guesses");
    }
    else
    {
        printf("You Win!");
    }

    return 0;
}