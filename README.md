# Group 4 – Design and Analysis of Algorithms (DAA) Macro Projects

> A collection of five algorithm projects covering all major topics in DAA —  
> Divide and Conquer, Dynamic Programming, Backtracking, and Branch and Bound.  
> Each unit contains a working implementation, an AI-generated visualization, and full documentation.

---

## Table of Contents

1. [Unit 1 – Sorting Complexity Visualizer](#unit-1--sorting-complexity-visualizer)
2. [Unit 2 – Strassen's Matrix Multiplication](#unit-2--strassens-matrix-multiplication)
3. [Unit 3 – 0/1 Knapsack using Dynamic Programming](#unit-3--01-knapsack-using-dynamic-programming)
4. [Unit 4 – N-Queens using Backtracking](#unit-4--n-queens-using-backtracking)
5. [Unit 5 – TSP using Branch and Bound](#unit-5--tsp-using-branch-and-bound)
6. [Technologies Used](#technologies-used)
7. [How to Run](#how-to-run)
8. [Project Structure](#project-structure)
9. [Team](#team)

---

## Unit 1 – Sorting Complexity Visualizer

**Folder:** `unit-1/unit-1/`  
**Language:** Python 3  
**Technique:** Divide and Conquer  
**Algorithms:** Merge Sort, Quick Sort

### Description

This project compares the practical execution time of **Merge Sort** and **Quick Sort** across three input sizes — n = 10, n = 100, and n = 1000 — and visualizes the results as a line graph.

Both algorithms are implemented from scratch without using Python's built-in `sort()` or `sorted()`.

### Problem Statement

Given random integer arrays of sizes 10, 100, and 1000, measure and compare the actual execution time of Merge Sort and Quick Sort, then plot the results.

### Algorithms

| Algorithm  | Strategy           | Best Case  | Average Case | Worst Case | Space    | Stable? |
|------------|--------------------|------------|--------------|------------|----------|---------|
| Merge Sort | Divide and Conquer | O(n log n) | O(n log n)   | O(n log n) | O(n)     | Yes     |
| Quick Sort | Divide and Conquer | O(n log n) | O(n log n)   | O(n²)      | O(log n) | No      |

### How Merge Sort Works

1. **Divide** — Split the array into two equal halves.
2. **Conquer** — Recursively sort each half.
3. **Combine** — Merge the two sorted halves by comparing elements one by one.

```
Original  :  [38, 27, 43, 3]
Divide    :  [38, 27]  [43, 3]
Divide    :  [38] [27]  [43] [3]
Merge     :  [27, 38]  [3, 43]
Merge     :  [3, 27, 38, 43]
```

### How Quick Sort Works

1. **Pick a Pivot** — Choose the last element as the pivot.
2. **Partition** — Move elements smaller than pivot to the left, larger to the right.
3. **Recurse** — Apply Quick Sort to the left and right partitions.

```
Original  :  [10, 3, 7, 1, 5]    Pivot = 5
Left      :  [3, 1]
Right     :  [10, 7]
Final     :  [1, 3, 5, 7, 10]
```

### Key Finding

Quick Sort is generally faster in practice due to better CPU cache behaviour and lower constant factors, even though both algorithms share an O(n log n) average complexity.

### Files

| File                    | Purpose                                        |
|-------------------------|------------------------------------------------|
| `main.py`               | Main script — timing, output, and graph        |
| `sorting.py`            | Merge Sort and Quick Sort implementations      |
| `sorting_complexity.png`| Output line graph comparing both algorithms    |
| `prompt.txt`            | AI prompt used to generate this project        |
| `README.md`             | Full documentation                             |

### How to Run

```bash
cd "unit-1/unit-1"
pip install matplotlib
python main.py
```

---

## Unit 2 – Strassen's Matrix Multiplication

**Folder:** `unit 2/`  
**Language:** Java  
**Technique:** Divide and Conquer  
**Algorithm:** Strassen's Matrix Multiplication

### Description

This project demonstrates matrix multiplication using **Strassen's Algorithm**, a Divide and Conquer technique that reduces the number of recursive multiplications from 8 to 7.

### Problem Statement

Given two square matrices A and B, multiply them using Strassen's Matrix Multiplication algorithm.

```
A = [ A11  A12 ]      B = [ B11  B12 ]
    [ A21  A22 ]          [ B21  B22 ]
```

### Algorithm — Seven Strassen Products

```
M1 = (A11 + A22)(B11 + B22)
M2 = (A21 + A22) × B11
M3 = A11 × (B12 - B22)
M4 = A22 × (B21 - B11)
M5 = (A11 + A12) × B22
M6 = (A21 - A11)(B11 + B12)
M7 = (A12 - A22)(B21 + B22)
```

Result matrix:

```
C11 = M1 + M4 - M5 + M7
C12 = M3 + M5
C21 = M2 + M4
C22 = M1 - M2 + M3 + M6
```

### Worked Example

```
A = [ 1  2 ]    B = [ 5  6 ]
    [ 3  4 ]        [ 7  8 ]

Result C = [ 19  22 ]
           [ 43  50 ]
```

### Time Complexity

| Method                  | Time Complexity |
|-------------------------|-----------------|
| Standard Multiplication | O(n³)           |
| Strassen's Algorithm    | O(n^log₂7) ≈ O(n^2.81) |

### Files

| File                     | Purpose                                       |
|--------------------------|-----------------------------------------------|
| `Project5_Strassen.java` | Java implementation of Strassen's Algorithm   |
| `Visualization.png`      | Visual breakdown of the divide-and-conquer    |
| `prompt.txt`             | AI prompt used to generate the visualization  |
| `README.md`              | Full documentation                            |

### How to Run

```bash
cd "unit 2"
javac Project5_Strassen.java
java Project5_Strassen
```

### Expected Output

```
Matrix A:
1 2
3 4

Matrix B:
5 6
7 8

Result Matrix:
19 22
43 50
```

---

## Unit 3 – 0/1 Knapsack using Dynamic Programming

**Folder:** `unit 3/`  
**Language:** Java  
**Technique:** Dynamic Programming  
**Algorithm:** 0/1 Knapsack

### Description

The **0/1 Knapsack** problem is a classic optimization problem solved using Dynamic Programming. Each item either gets selected (1) or not (0) — it cannot be divided.

### Problem Statement

Select items from the list below to maximize profit without exceeding the knapsack capacity of 10.

| Item   | Weight | Profit |
|--------|--------|--------|
| Item 1 | 2      | 3      |
| Item 2 | 3      | 4      |
| Item 3 | 4      | 5      |
| Item 4 | 5      | 6      |

**Knapsack Capacity:** 10

### Algorithm

For each item and each capacity:

- **Include** — Add its profit to the best solution for the remaining capacity.
- **Exclude** — Keep the best solution without this item.
- Store the maximum of the two choices in the DP table.

### DP Table

```
         Capacity →
         0  1  2  3  4  5  6  7  8  9  10
0        0  0  0  0  0  0  0  0  0  0   0
Item 1   0  0  3  3  3  3  3  3  3  3   3
Item 2   0  0  3  4  4  7  7  7  7  7   7
Item 3   0  0  3  4  5  7  8  9  9  9  12
Item 4   0  0  3  4  5  7  8  9 10 11  13
```

### Optimal Solution

- **Maximum Profit = 13**
- **Selected Items:** Item 1 + Item 2 + Item 4
- **Total Weight:** 2 + 3 + 5 = 10
- **Total Profit:** 3 + 4 + 6 = 13

### Time and Space Complexity

| Complexity | Value      |
|------------|------------|
| Time       | O(n × W)   |
| Space      | O(n × W)   |

where n = number of items, W = knapsack capacity.

### Files

| File                      | Purpose                                          |
|---------------------------|--------------------------------------------------|
| `Project9_Knapsack.java`  | Java implementation of 0/1 Knapsack using DP     |
| `Visualization.png`       | DP table visualization                           |
| `Prompt.txt`              | AI prompt used to generate the visualization     |
| `README.md`               | Full documentation                               |

### How to Run

```bash
cd "unit 3"
javac Project9_Knapsack.java
java Project9_Knapsack
```

### Expected Output

```
DP Table:
0   0   0   0   0   0   0   0   0   0   0
0   0   3   3   3   3   3   3   3   3   3
0   0   3   4   4   7   7   7   7   7   7
0   0   3   4   5   7   8   9   9   9   12
0   0   3   4   5   7   8   9   10  11  13
Maximum Profit = 13
```

---

## Unit 4 – N-Queens using Backtracking

**Folder:** `unit-4/`  
**Language:** Java  
**Technique:** Backtracking  
**Algorithm:** N-Queens (N = 4)

### Description

The **N-Queens** problem asks us to place N queens on an N × N chessboard such that no two queens attack each other. This project solves it for N = 4 using the **Backtracking** technique and includes an AI-generated state-space tree.

### Problem Statement

Place 4 queens on a 4 × 4 chessboard such that no two queens share the same:

- Row
- Column
- Diagonal

### Algorithm

1. Start from row 0.
2. Try placing a queen in every column of the current row.
3. Check if the placement is safe (no conflict with queens already placed).
4. If safe, place the queen and move to the next row recursively.
5. If no safe column exists in the current row, **backtrack** to the previous row.
6. Remove the previously placed queen and try another column.
7. Repeat until all 4 queens are placed.

### Backtracking Logic

```
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
```

### Solutions for N = 4

**Solution 1:**
```
. Q . .
. . . Q
Q . . .
. . Q .
```

**Solution 2:**
```
. . Q .
Q . . .
. . . Q
. Q . .
```

**Total Solutions = 2**

### Complexity Analysis

| Complexity | Value  |
|------------|--------|
| Time       | O(N!)  |
| Space      | O(N)   |

### Files

| File                      | Purpose                                           |
|---------------------------|---------------------------------------------------|
| `Project10_NQueens.java`  | Java implementation of N-Queens using Backtracking|
| `visualization.png`       | State-space tree visualization                    |
| `Prompt.txt`              | AI prompt used to generate the visualization      |
| `README.md`               | Full documentation                                |

### How to Run

```bash
cd "unit-4"
javac Project10_NQueens.java
java Project10_NQueens
```

### Expected Output

```
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

## Unit 5 – TSP using Branch and Bound

**Folder:** `unit-5/`  
**Language:** Java  
**Technique:** Branch and Bound  
**Algorithm:** Travelling Salesperson Problem (TSP)

### Description

The **Travelling Salesperson Problem (TSP)** asks for the minimum-cost tour that visits every city exactly once and returns to the starting city. This project solves it for 4 cities using the **Branch and Bound** technique.

### Problem Statement

Find the minimum-cost route starting from city A, visiting cities B, C, and D exactly once, and returning to A.

**Cost Matrix:**

```
    A   B   C   D
A   0  10  15  20
B  10   0  35  25
C  15  35   0  30
D  20  25  30   0
```

### Algorithm

1. Start from city A.
2. Generate branches for all unvisited cities.
3. Calculate the cost and lower bound for each branch.
4. Select the most promising branch (lowest bound).
5. Prune any branch whose bound ≥ current best cost.
6. Continue until all cities are visited and the tour returns to A.
7. Return the tour with the minimum total cost.

### All Possible Tours

| Tour                  | Cost Calculation           | Total |
|-----------------------|----------------------------|-------|
| A → B → C → D → A    | 10 + 35 + 30 + 20          | 95    |
| A → B → D → C → A    | 10 + 25 + 30 + 15          | **80** |
| A → C → B → D → A    | 15 + 35 + 25 + 20          | 95    |
| A → C → D → B → A    | 15 + 30 + 25 + 10          | **80** |
| A → D → B → C → A    | 20 + 25 + 35 + 15          | 95    |
| A → D → C → B → A    | 20 + 30 + 35 + 10          | 95    |

### Optimal Result

- **Optimal Tour:** A → B → D → C → A
- **Minimum Cost:** 80
- (The reverse tour A → C → D → B → A also costs 80)

### Pruning

Once the best cost of 80 is found, any branch with a bound ≥ 80 is pruned, avoiding unnecessary exploration.

### Files

| File                                    | Purpose                                          |
|-----------------------------------------|--------------------------------------------------|
| `Project14_TSP_BranchAndBound.java`     | Java implementation of TSP using Branch & Bound  |
| `Visualization.png`                     | Branch and Bound search tree visualization       |
| `Prompt.txt`                            | AI prompt used to generate the visualization     |
| `Readme.md`                             | Full documentation                               |

### How to Run

```bash
cd "unit-5"
javac Project14_TSP_BranchAndBound.java.java
java Project14_TSP_BranchAndBound
```

### Expected Output

```
TSP using Branch and Bound
--------------------------
Cost Matrix:
0   10  15  20
10  0   35  25
15  35  0   30
20  25  30  0

Search Process:
...

Optimal Tour:
A -> B -> D -> C -> A
Minimum Cost = 80
```

---

## Technologies Used

| Technology  | Units        | Purpose                                       |
|-------------|--------------|-----------------------------------------------|
| Python 3    | Unit 1       | Algorithm implementation and visualization    |
| Matplotlib  | Unit 1       | Line graph generation                         |
| Java        | Units 2–5    | Algorithm implementation                      |
| AI Tools    | All units    | Visualization and documentation generation    |
| Markdown    | All units    | Project documentation                         |

---

## How to Run

### Unit 1 (Python)

```bash
cd "unit-1/unit-1"
pip install matplotlib
python main.py
```

### Units 2–5 (Java)

```bash
# Unit 2
cd "unit 2"
javac Project5_Strassen.java
java Project5_Strassen

# Unit 3
cd "unit 3"
javac Project9_Knapsack.java
java Project9_Knapsack

# Unit 4
cd "unit-4"
javac Project10_NQueens.java
java Project10_NQueens

# Unit 5
cd "unit-5"
javac Project14_TSP_BranchAndBound.java.java
java Project14_TSP_BranchAndBound
```

**Requirements:**
- Python 3.x with pip (for Unit 1)
- Java Development Kit (JDK) 8 or above (for Units 2–5)

---

## Project Structure

```
Group-4/
│
├── README.md                          ← This file (main overview)
│
├── unit-1/
│   └── unit-1/
│       ├── main.py
│       ├── sorting.py
│       ├── sorting_complexity.png
│       ├── prompt.txt
│       └── README.md
│
├── unit 2/
│   ├── Project5_Strassen.java
│   ├── Visualization.png
│   ├── prompt.txt
│   └── README.md
│
├── unit 3/
│   ├── Project9_Knapsack.java
│   ├── Visualization.png
│   ├── Prompt.txt
│   └── README.md
│
├── unit-4/
│   ├── Project10_NQueens.java
│   ├── visualization.png
│   ├── Prompt.txt
│   └── README.md
│
└── unit-5/
    ├── Project14_TSP_BranchAndBound.java
    ├── Visualization.png
    ├── Prompt.txt
    └── Readme.md
```

---

## Algorithm Summary

| Unit   | Project             | Algorithm               | Technique          | Language | Complexity       |
|--------|---------------------|-------------------------|--------------------|----------|------------------|
| Unit 1 | Sorting Visualizer  | Merge Sort, Quick Sort  | Divide and Conquer | Python   | O(n log n) avg   |
| Unit 2 | Matrix Multiply     | Strassen's Algorithm    | Divide and Conquer | Java     | O(n^2.81)        |
| Unit 3 | Knapsack            | 0/1 Knapsack (DP)       | Dynamic Programming| Java     | O(n × W)         |
| Unit 4 | N-Queens            | Backtracking            | Backtracking       | Java     | O(N!)            |
| Unit 5 | TSP                 | Branch and Bound        | Branch and Bound   | Java     | Exponential (pruned) |

---

## Team

**Group 4**  
Subject: Design and Analysis of Algorithms (DAA)

---

*Submitted as DAA Macro Projects*  
*Subject: Design and Analysis of Algorithms*
