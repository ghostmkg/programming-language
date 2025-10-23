public class transposeOfAMatrix {
    public static void main(String[] args) {
        int[][] Array = {
                { 5, 6, 1, 2 },
                { 3, 8, 7, 0 },
                { 10, 9, 8, 6 },
                { 1, 3, 5, 9 }
        };
        transform(Array);
        print(Array);
    }

    
    public static void transform(int[][] A) {
        int N = A.length;
        for (int row = 0; row < N; row++) {
            for (int col = 0; col < N; col++) {
                if (row != col && row<col) {
                    int temp = A[row][col];
                    A[row][col] = A[col][row];
                    A[col][row] = temp;
                }
            }
        }
    }
 


    public static void print(int[][] A) {
        for (int row = 0; row < A.length; row++) {
            for (int col = 0; col < A[0].length; col++) {
                System.out.print(A[row][col] + " ");
            }
            System.out.println();
        }
    }
}

