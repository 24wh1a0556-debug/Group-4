import java.util.*;

public class Project10_NQueens {

    static int N = 4;
    static int[] board = new int[N];
    static int solutionCount = 0;

    // Checks whether a queen can be placed
    // at the given row and column
    static boolean isSafe(int row, int col) {

        for (int i = 0; i < row; i++) {

            // Check same column
            if (board[i] == col) {
                return false;
            }

            // Check same diagonal
            if (Math.abs(board[i] - col) == Math.abs(i - row)) {
                return false;
            }
        }

        return true;
    }

    // Backtracking function
    static void solveNQueens(int row) {

        // All queens have been placed
        if (row == N) {
            solutionCount++;

            System.out.println("\nSolution " + solutionCount + ":");
            printBoard();

            return;
        }

        // Try every column
        for (int col = 0; col < N; col++) {

            if (isSafe(row, col)) {

                // Place queen
                board[row] = col;

                // Move to next row
                solveNQueens(row + 1);

                // Backtrack
                board[row] = -1;
            }
        }
    }

    // Prints the chessboard
    static void printBoard() {

        for (int i = 0; i < N; i++) {

            for (int j = 0; j < N; j++) {

                if (board[i] == j) {
                    System.out.print("Q ");
                } else {
                    System.out.print(". ");
                }
            }

            System.out.println();
        }
    }

    public static void main(String[] args) {

        Arrays.fill(board, -1);

        System.out.println("N-Queens Problem");
        System.out.println("N = " + N);

        solveNQueens(0);

        System.out.println("\nTotal Solutions = " + solutionCount);
    }
}