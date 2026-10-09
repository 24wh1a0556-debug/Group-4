# Project 5 – Divide-and-Conquer Matrix Multiplication using Strassen's Algorithm

## Description

This project demonstrates matrix multiplication using Strassen's Algorithm, which is a divide-and-conquer technique.

Instead of directly multiplying two matrices using the normal method, Strassen's algorithm divides each matrix into smaller submatrices and recursively performs the multiplication. It uses seven multiplication operations instead of eight for each division.

## Problem

Given two square matrices A and B, multiply them using Strassen's Matrix Multiplication algorithm.

The matrices are divided into four smaller parts:

A = [ A11  A12 ]
    [ A21  A22 ]

B = [ B11  B12 ]
    [ B21  B22 ]

## Algorithm

1. Take two square matrices A and B.
2. If the matrix size is 1 × 1, multiply the two elements directly.
3. Divide A into A11, A12, A21 and A22.
4. Divide B into B11, B12, B21 and B22.
5. Calculate the seven Strassen products:
   - M1 = (A11 + A22)(B11 + B22)
   - M2 = (A21 + A22)B11
   - M3 = A11(B12 - B22)
   - M4 = A22(B21 - B11)
   - M5 = (A11 + A12)B22
   - M6 = (A21 - A11)(B11 + B12)
   - M7 = (A12 - A22)(B21 + B22)
6. Calculate:
   - C11 = M1 + M4 - M5 + M7
   - C12 = M3 + M5
   - C21 = M2 + M4
   - C22 = M1 - M2 + M3 + M6
7. Combine the four parts to get the final matrix C.

## Pseudocode

```text
Algorithm Strassen(A, B)

If matrix size is 1:
    return A × B

Divide A into A11, A12, A21, A22
Divide B into B11, B12, B21, B22

M1 = Strassen(A11 + A22, B11 + B22)
M2 = Strassen(A21 + A22, B11)
M3 = Strassen(A11, B12 - B22)
M4 = Strassen(A22, B21 - B11)
M5 = Strassen(A11 + A12, B22)
M6 = Strassen(A21 - A11, B11 + B12)
M7 = Strassen(A12 - A22, B21 + B22)

C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6

Combine C11, C12, C21, C22

Return C
```

## Algorithm Explanation

Strassen's algorithm follows the divide-and-conquer approach. The matrices are divided into smaller matrices until the base case is reached.

The main difference from normal matrix multiplication is that Strassen's method calculates seven recursive products instead of eight. The results are then combined using additions and subtractions to form the final matrix.


## Example

Consider the following two 2 × 2 matrices:

```text
A = [ 1  2 ]
    [ 3  4 ]

B = [ 5  6 ]
    [ 7  8 ]
```

For a 2 × 2 matrix, the four parts are single elements:

```text
A11 = 1    A12 = 2
A21 = 3    A22 = 4

B11 = 5    B12 = 6
B21 = 7    B22 = 8
```

Using Strassen's seven formulas:

```text
M1 = (A11 + A22)(B11 + B22)
   = (1 + 4)(5 + 8)
   = 65

M2 = (A21 + A22)B11
   = (3 + 4)(5)
   = 35

M3 = A11(B12 - B22)
   = 1(6 - 8)
   = -2

M4 = A22(B21 - B11)
   = 4(7 - 5)
   = 8

M5 = (A11 + A12)B22
   = (1 + 2)(8)
   = 24

M6 = (A21 - A11)(B11 + B12)
   = (3 - 1)(5 + 6)
   = 22

M7 = (A12 - A22)(B21 + B22)
   = (2 - 4)(7 + 8)
   = -30
```

Now calculate the result matrix:

```text
C11 = M1 + M4 - M5 + M7
    = 65 + 8 - 24 - 30
    = 19

C12 = M3 + M5
    = -2 + 24
    = 22

C21 = M2 + M4
    = 35 + 8
    = 43

C22 = M1 - M2 + M3 + M6
    = 65 - 35 - 2 + 22
    = 50
```

Therefore:

```text
C = [ 19  22 ]
    [ 43  50 ]
```

So, the multiplication of A and B gives the final matrix C.

## Visualization Explanation

The visualization shows how the original matrices are divided into four submatrices. It also shows the seven Strassen multiplication steps and how their results are combined to form C11, C12, C21 and C22.

This makes the divide-and-conquer process easier to understand.

## Time Complexity

- Standard Matrix Multiplication: O(n³)
- Strassen's Algorithm: O(n^log₂7)
- Approximately: O(n^2.81)

## Prompt Used

Create a clean academic visualization for Divide-and-Conquer Matrix Multiplication using Strassen's Algorithm.

Show:
1. Two input matrices A and B.
2. Division of each matrix into four submatrices.
3. The seven Strassen multiplication operations M1 to M7.
4. The formulas for C11, C12, C21 and C22.
5. How the four result submatrices are combined into the final matrix C.
6. The divide-and-conquer flow from the original matrices to smaller matrices and then back to the final result.
7. Use a clean and simple academic style suitable for a DAA college project, PPT and README.
8. Make all formulas mathematically correct and clearly readable.

## Learning Outcome

- Understood the divide-and-conquer approach.
- Learned how Strassen's matrix multiplication works.
- Understood how seven recursive multiplications are used instead of eight.
- Learned how to represent an algorithm using a visualization.
- Practiced documenting a DAA project for GitHub.
