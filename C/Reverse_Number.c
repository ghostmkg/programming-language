#include <stdio.h>

int main() {
    int num, reversed = 0;

    printf("Enter a number: ");
    scanf("%d", &num);

    while (num != 0) {
        int digit = num % 10;         // Get last digit
        reversed = reversed * 10 + digit; // Append digit
        num /= 10;                    // Remove last digit
    }

    printf("Reversed number: %d\n", reversed);

    return 0;
}