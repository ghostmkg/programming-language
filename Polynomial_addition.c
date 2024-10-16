#include <stdio.h>
#include <stdlib.h>
int* createPolynomial(int degree) {
    int *poly = (int*)malloc((degree + 1) * sizeof(int));
    if (poly == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    return poly;
}
void inputPolynomial(int* poly, int degree) {
    printf("Enter the coefficients of the polynomial (from highest to lowest degree):\n");
    for (int i = degree; i >= 0; i--) {
        printf("Coefficient of x^%d: ", i);
        scanf("%d", &poly[i]);
    }
}

// Function to display a polynomial
void displayPolynomial(int* poly, int degree) {
    for (int i = degree; i >= 0; i--) {
        if (poly[i] != 0) {
            printf("%d", poly[i]);
            if (i > 0) {
                printf("x^%d", i);
                if (poly[i - 1] >= 0) printf(" + ");
            }
        }
    }
    printf("\n");
}

// Function to add two polynomials
int* addPolynomials(int* poly1, int* poly2, int degree1, int degree2) {
    int maxDegree = (degree1 > degree2) ? degree1 : degree2;
    int *result = createPolynomial(maxDegree);

    for (int i = 0; i <= maxDegree; i++) {
        int coeff1 = (i <= degree1) ? poly1[i] : 0;
        int coeff2 = (i <= degree2) ? poly2[i] : 0;
        result[i] = coeff1 + coeff2;
    }

    return result;
}
int main() {
    int degree1, degree2;

    // Input the degree of the first polynomial
    printf("Enter the highest degree of the first polynomial: ");
    scanf("%d", &degree1);
    int *poly1 = createPolynomial(degree1);
    inputPolynomial(poly1, degree1);

    // Input the degree of the second polynomial
    printf("Enter the highest degree of the second polynomial: ");
    scanf("%d", &degree2);
    int *poly2 = createPolynomial(degree2);
    inputPolynomial(poly2, degree2);

    // Add the polynomials
    int *sum = addPolynomials(poly1, poly2, degree1, degree2);
    printf("\nSum of the polynomials: ");
    displayPolynomial(sum, (degree1 > degree2) ? degree1 : degree2);
    // Free the dynamically allocated memory
    free(poly1);
    free(poly2);
    free(sum);

    return 0;
}
