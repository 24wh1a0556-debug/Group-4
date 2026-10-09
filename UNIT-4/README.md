# N-Queens Problem using Backtracking

## Project Information

**Subject:** Design and Analysis of Algorithms (DAA)

**Unit:** Unit IV – Backtracking

**Project:** Project 10 – N-Queens State Space Tree

**Algorithm:** Backtracking

**N:** 4

---

## 1. Description

The N-Queens problem is a classical problem in Design and Analysis of Algorithms. The objective is to place N queens on an N × N chessboard such that no two queens attack each other.

In this project, the N-Queens problem is implemented using the Backtracking technique for N = 4.

A state-space tree is also generated using AI-based visualization to show the recursive exploration of possible queen placements, invalid branches, backtracking, and final solutions.

---

## 2. Objective

The objectives of this project are:

* To implement the N-Queens problem using Backtracking.
* To understand recursive problem solving.
* To visualize the state-space tree for N = 4.
* To identify valid and invalid queen placements.
* To understand how backtracking removes invalid choices.
* To demonstrate the use of AI for algorithm visualization.

---

## 3. Problem Statement

Place 4 queens on a 4 × 4 chessboard such that no two queens attack each other.

Two queens must not be placed in:

* The same row.
* The same column.
* The same diagonal.

---

## 4. Algorithm Used

The Backtracking technique is used.

The algorithm places one queen in each row.

### Steps

1. Start from the first row.
2. Try placing a queen in every column.
3. Check whether the selected position is safe.
4. If the position is safe, place the queen.
5. Move to the next row recursively.
6. If no safe position is available, backtrack to the previous row.
7. Remove the previously placed queen.
8. Try another column.
9. Continue until all queens are placed successfully.

---

## 5. Pseudocode

```text
NQueens(row)

    if row == N
        print solution
        return

    for column = 0 to N-1

        if position(row, column) is safe

            place queen

            NQueens(row + 1)

            remove queen
```

### Safe Position

A position is safe when:

```text
No queen exists in the same column
AND
No queen exists on the same diagonal
```

---

## 6. Backtracking Logic

Backtracking works by making a choice and continuing with it only if the choice is valid.

If the algorithm reaches a situation where no valid position is available, it returns to the previous decision and tries another possibility.

For example:

```text
Place Queen
     ↓
Check Position
     ↓
Is it safe?
   /     \
 No       Yes
 ↓         ↓
Reject   Continue
           ↓
       Next Row
           ↓
      No valid choice
           ↓
       Backtrack
           ↓
     Try another column
```

---

## 7. AI Prompt Used

The following prompt was used to generate the state-space tree visualization:

> Create a clear educational state-space tree visualization for the N-Queens problem using backtracking with N = 4. Show the root node as "Start". At each level, represent the placement of one queen in the next row of a 4×4 chessboard. Show possible column choices, valid and invalid placements, backtracking steps, and the two complete solutions. Use green for valid choices, red for invalid/pruned branches, blue for backtracking, and highlight complete solutions. Use a clean academic style suitable for a third-year computer science DAA project.

The complete prompt is available in `Prompt.txt`.

---

## 8. State-Space Tree Visualization

The generated visualization represents the recursive exploration of the N-Queens problem.

* **Green:** Valid choice
* **Red:** Invalid or pruned branch
* **Blue:** Backtracking
* **Highlighted:** Complete solution

The visualization is available in:

`Visualization.png`

---

## 9. Solutions for N = 4

The algorithm finds two valid solutions.

### Solution 1

```text
. Q . .
. . . Q
Q . . .
. . Q .
```

### Solution 2

```text
. . Q .
Q . . .
. . . Q
. Q . .
```

Therefore:

```text
Total number of solutions = 2
```

---

## 10. Program Output

```text
N-Queens Problem
N = 4

Solution 1:
. Q . .
. . . Q
Q . . .
. . Q .

Solution 2:
. . Q .
Q . . .
. . . Q
. Q . .

Total Solutions = 2
```

---

## 11. Complexity Analysis

### Time Complexity

The worst-case time complexity is approximately:

```text
O(N!)
```

The algorithm explores different possible placements of queens and prunes invalid branches.

### Space Complexity

```text
O(N)
```

Space is required for the board representation and recursion stack, excluding storage for all solutions.

---

## 12. Technologies Used

* Java
* Backtracking
* Artificial Intelligence for visualization
* GitHub
* Markdown

---

## 13. Learning Outcomes

After completing this project, the following concepts were understood:

* N-Queens problem.
* Backtracking technique.
* Recursion.
* State-space trees.
* Branch pruning.
* Valid and invalid states.
* AI-based algorithm visualization.
* GitHub project documentation.

---

## 14. Files in This Project

```text
Unit4_Backtracking/
│
├── Project10_NQueens.java
├── Prompt.txt
├── Visualization.png
└── README.md
```

### File Description

| File                     | Purpose                                            |
| ------------------------ | -------------------------------------------------- |
| `Project10_NQueens.java` | Java implementation of N-Queens using Backtracking |
| `Prompt.txt`             | AI prompt used to generate the visualization       |
| `Visualization.png`      | State-space tree visualization                     |
| `README.md`              | Complete project documentation                     |

---

## 15. Conclusion

The N-Queens problem demonstrates how Backtracking can efficiently explore a large solution space by eliminating invalid choices early.

For N = 4, the algorithm explores possible queen placements, backtracks whenever a placement becomes invalid, and finally finds two valid solutions.

The state-space tree provides a visual representation of this recursive process and makes the working of the Backtracking algorithm easier to understand.
