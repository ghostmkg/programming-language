#include <stdio.h>
#include <string.h>

int main() {
    char str[100], reversed[100];
    int length, i, isPalindrome = 1;

    printf("Enter a word: ");
    scanf("%s", str);  // Reads a single word (no spaces)

    length = strlen(str);

    // Reverse the string
    for (i = 0; i < length; i++) {
        reversed[i] = str[length - i - 1];
    }
    reversed[length] = '\0';  // Null-terminate the reversed string

    // Compare original and reversed
    for (i = 0; i < length; i++) {
        if (str[i] != reversed[i]) {
            isPalindrome = 0;
            break;
        }
    }

    if (isPalindrome) {
        printf("✅ It's a palindrome!\n");
    } else {
        printf("❌ Not a palindrome.\n");
    }

    return 0;
}