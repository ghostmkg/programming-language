package opensource;
public class TransposeOfAMatrix {
    // Method to calculate the transpose of a square matrix
    public static void calculateTranspose(int mat[][]) {
        int N = mat.length; // Get the number of rows (and columns, since it's a square matrix)    
        // Loop through each row of the matrix
        for (int row = 0; row < N; row++) {
            // Loop through each column, starting from row + 1 to avoid swapping back
            for (int col = row + 1; col < N; col++) {
                // Swap the elements at (row, col) and (col, row)
                int temp = mat[row][col];
                mat[row][col] = mat[col][row];
                mat[col][row] = temp;
            }
        }
        // Print the transposed matrix
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                System.out.print(mat[row][col] + " "); // Print each element with a space
            }
            System.out.println(); // Move to the next line after printing a row
        }
    }

    public static void main(String[] args) {
        // Initialize a square matrix
        int mat[][] = {
            {1, 2, 3},
            {4, 5, 6},
            {7, 8, 9}
        };

        // Get the number of rows and columns
        int n = mat.length; // Number of rows
        int m = mat[0].length; // Number of columns

        // Check if the matrix is square; if not, exit the method
        if (n != m) {
            System.out.println("Matrix is not square. Transpose cannot be calculated in place.");
            return; // Exit if the matrix is not square
        }
        // Calculate and print the transpose of the matrix
        calculateTranspose(mat);
    }
}

