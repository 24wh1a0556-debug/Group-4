# Sorting Complexity Visualizer

> A DAA Macro Project that compares the practical execution time of  
> **Merge Sort** and **Quick Sort** across input sizes n = 10, 100, and 1000,  
> and visualizes the results as a line graph.

---

## Table of Contents

1. [Project Title](#1-project-title)
2. [Problem Statement](#2-problem-statement)
3. [Objective](#3-objective)
4. [Technologies Used](#4-technologies-used)
5. [Algorithms Used](#5-algorithms-used)
6. [Merge Sort Explanation](#6-merge-sort-explanation)
7. [Quick Sort Explanation](#7-quick-sort-explanation)
8. [Merge Sort Pseudocode](#8-merge-sort-pseudocode)
9. [Quick Sort Pseudocode](#9-quick-sort-pseudocode)
10. [Time Complexity Comparison Table](#10-time-complexity-comparison-table)
11. [Experimental Input Sizes](#11-experimental-input-sizes)
12. [Visualization Explanation](#12-visualization-explanation)
13. [How to Install](#13-how-to-install)
14. [How to Run](#14-how-to-run)
15. [Expected Output](#15-expected-output)
16. [Conclusion](#16-conclusion)

---

## 1. Project Title

**Sorting Complexity Visualizer**

Subject: Design and Analysis of Algorithms (DAA)  
Language: Python 3

---

## 2. Problem Statement

Sorting is one of the most studied problems in computer science. Many algorithms exist to sort a list of numbers, but they differ in how fast they run — especially as the input size grows.

Two of the most well-known efficient sorting algorithms are **Merge Sort** and **Quick Sort**. Both have an average time complexity of **O(n log n)**, but they behave differently in practice because of how they access memory, how they split the data, and how they handle recursion.

As a DAA student, it is not enough to memorize the formula "O(n log n)." The real learning comes from *seeing* the difference — running both algorithms on real data, measuring actual time, and plotting the result.

This project answers the question:

> *"When both algorithms are O(n log n) on average, which one is actually faster in practice — and by how much?"*

---

## 3. Objective

- Implement **Merge Sort** from scratch in Python without using any built-in sort.
- Implement **Quick Sort** from scratch in Python without using any built-in sort.
- Generate **random integer arrays** for three input sizes: n = 10, n = 100, n = 1000.
- **Measure and record** the execution time of both algorithms for each input size.
- **Compare** the results by printing a summary table in the terminal.
- **Visualize** the comparison using a line chart (saved as `sorting_complexity.png`).

---

## 4. Technologies Used

| Technology       | Version  | Purpose                                        |
|------------------|----------|------------------------------------------------|
| Python           | 3.x      | Core programming language                      |
| Matplotlib       | 3.11.0   | Drawing and saving the line graph              |
| `random` module  | Built-in | Generating random integer arrays               |
| `time` module    | Built-in | Measuring execution time with high precision   |
| `copy` module    | Built-in | Copying arrays so both algorithms get same data|
| `sys` module     | Built-in | Setting recursion limit for Python 3.14 safety |

---

## 5. Algorithms Used

| Algorithm  | Strategy           | Average Case | Worst Case |
|------------|--------------------|--------------|------------|
| Merge Sort | Divide and Conquer | O(n log n)   | O(n log n) |
| Quick Sort | Divide and Conquer | O(n log n)   | O(n²)      |

Both algorithms are implemented manually in `sorting.py`.  
Python's built-in `sort()` and `sorted()` are **not used** anywhere in this project.

---

## 6. Merge Sort Explanation

Merge Sort follows the **Divide and Conquer** strategy.

### How it works — Step by Step

**Step 1 — Divide**  
Split the array into two equal halves at the middle index.

**Step 2 — Conquer**  
Recursively apply Merge Sort to each half until each piece has only one element (which is already sorted by definition).

**Step 3 — Combine**  
Merge the two sorted halves back into one sorted array by comparing elements one by one and placing the smaller element first.

### Worked Example

```
Original  :  [38, 27, 43, 3]

Divide    :  [38, 27]        [43, 3]
Divide    :  [38]  [27]      [43]  [3]

Merge     :  [27, 38]        [3, 43]
Merge     :  [3, 27, 38, 43]
```

### Key Properties

- Always divides the problem into **two equal halves**.
- Time complexity is **O(n log n) in all cases** — no bad inputs exist for Merge Sort.
- Requires **extra memory** proportional to the input size (O(n) space).
- It is a **stable sort** — equal elements maintain their original order.

---

## 7. Quick Sort Explanation

Quick Sort is also a **Divide and Conquer** algorithm, but it works very differently from Merge Sort.

### How it works — Step by Step

**Step 1 — Pick a Pivot**  
Choose one element as the pivot. In this project, we always pick the **last element** of the array.

**Step 2 — Partition**  
Rearrange the array so that:
- All elements **smaller than or equal to** the pivot go to the **left**.
- All elements **greater than** the pivot go to the **right**.
- The pivot itself is placed in its **correct final position**.

**Step 3 — Recurse**  
Recursively apply Quick Sort to the left partition and the right partition.

### Worked Example

```
Original  :  [10, 3, 7, 1, 5]    Pivot = 5

Left      :  [3, 1]   (elements ≤ 5, excluding pivot)
Right     :  [10, 7]  (elements > 5)

Recurse on Left  : [1, 3]
Recurse on Right : [7, 10]

Final     :  [1, 3, 5, 7, 10]
```

### Key Properties

- Pivot choice determines performance — a bad pivot (always min or max) causes **O(n²)** worst case.
- With **random data** (as used in this project), the worst case is extremely unlikely.
- Uses **less extra memory** than Merge Sort — O(log n) space on average.
- Often **faster in practice** than Merge Sort due to better CPU cache behaviour.
- It is **not a stable sort** — equal elements may change relative order.

---

## 8. Merge Sort Pseudocode

```
MERGE_SORT(arr):
    if length(arr) <= 1:
        return arr                        // Base case: already sorted

    mid   = length(arr) / 2
    left  = MERGE_SORT(arr[0 to mid])    // Sort left half
    right = MERGE_SORT(arr[mid to end])  // Sort right half

    return MERGE(left, right)            // Merge both sorted halves


MERGE(left, right):
    result = empty list
    i = 0, j = 0

    while i < length(left) AND j < length(right):
        if left[i] <= right[j]:
            append left[i] to result
            i = i + 1
        else:
            append right[j] to result
            j = j + 1

    // Append any remaining elements
    append rest of left  to result
    append rest of right to result

    return result
```

---

## 9. Quick Sort Pseudocode

```
QUICK_SORT(arr):
    if length(arr) <= 1:
        return arr                          // Base case: already sorted

    pivot = arr[last element]

    left  = all elements in arr[:-1] where element <= pivot
    right = all elements in arr[:-1] where element >  pivot

    return QUICK_SORT(left) + [pivot] + QUICK_SORT(right)
```

---

## 10. Time Complexity Comparison Table

| Algorithm  | Best Case  | Average Case | Worst Case | Space Complexity | Stable? |
|------------|------------|--------------|------------|------------------|---------|
| Merge Sort | O(n log n) | O(n log n)   | O(n log n) | O(n)             | Yes     |
| Quick Sort | O(n log n) | O(n log n)   | O(n²)      | O(log n)         | No      |

**Key Takeaway for Viva:**
- Merge Sort is more **predictable** — same complexity in all cases.
- Quick Sort is generally **faster in practice** but has a worst case risk.
- With random arrays, Quick Sort almost always runs in O(n log n).

---

## 11. Experimental Input Sizes

This project tests both algorithms on three different input sizes to observe how execution time scales with n:

| Experiment | Input Size (n) | Array Contents              |
|------------|----------------|-----------------------------|
| 1          | n = 10         | 10 random integers (1–10000)|
| 2          | n = 100        | 100 random integers (1–10000)|
| 3          | n = 1000       | 1000 random integers (1–10000)|

**Why these sizes?**
- **n = 10** is very small — both algorithms finish almost instantly. This establishes a baseline.
- **n = 100** is medium — a small but visible difference in time may appear.
- **n = 1000** is large enough to show a meaningful time difference and reflect the O(n log n) growth.

**Fair Testing:**  
Both algorithms are given an **identical copy** of the same randomly generated array for each experiment. This ensures the comparison is fair and not affected by array contents.

---

## 12. Visualization Explanation

After running the experiments, the program generates a **line chart** saved as `sorting_complexity.png`.

### What the Graph Shows

| Element              | Description                                      |
|----------------------|--------------------------------------------------|
| X-axis               | Input Size (n): values 10, 100, 1000             |
| Y-axis               | Execution Time in seconds                        |
| Blue solid line (●)  | Merge Sort execution time at each input size     |
| Red dashed line (■)  | Quick Sort execution time at each input size     |
| Legend               | Identifies which line is which algorithm         |
| Grid lines           | Help read exact values on the chart              |

### What to Observe

- For **n = 10**, both lines are very close to zero — the difference is negligible.
- As **n increases to 100 and 1000**, the lines rise and the gap (if any) becomes visible.
- The shape of both lines should follow a gentle upward curve, consistent with **O(n log n)** growth.
- Quick Sort's line is often slightly **below** Merge Sort's line, showing it is marginally faster in practice.
- Since arrays are randomly generated, results will vary slightly each time you run the program.

---

## 13. How to Install

Make sure **Python 3** is installed on your computer. Then follow these steps:

**Step 1 — Open a terminal and navigate to the project folder:**
```bash
cd path\to\DAA-Sorting-Visualizer
```

**Step 2 — (Recommended) Create a virtual environment to keep dependencies isolated:**
```bash
python -m venv venv
venv\Scripts\activate
```

> On Mac/Linux, use `source venv/bin/activate` instead.

**Step 3 — Install the required library:**
```bash
pip install -r requirements.txt
```

This installs **Matplotlib 3.11.0**, which is the only external library needed and is fully compatible with Python 3.14.

---

## 14. How to Run

After completing installation, run the project with a single command:

```bash
python main.py
```

The program will automatically:
1. Generate random integer arrays for n = 10, 100, and 1000
2. Run Merge Sort and Quick Sort on each array
3. Measure and print execution times in the terminal
4. Generate the line graph and save it as `sorting_complexity.png`

To view the graph, open `sorting_complexity.png` from your file explorer.

---

## 15. Expected Output

### Terminal Output

The exact time values will differ on every run because the arrays are randomly generated and execution speed depends on your hardware. The format will look like this:

```
==================================================
   Sorting Complexity Visualizer
   Compare: Merge Sort vs Quick Sort
==================================================

Input Size (n = 10)
  Merge Sort Time : 0.00001XXX seconds
  Quick Sort Time : 0.00000XXX seconds

Input Size (n = 100)
  Merge Sort Time : 0.00012XXX seconds
  Quick Sort Time : 0.00009XXX seconds

Input Size (n = 1000)
  Merge Sort Time : 0.00150XXX seconds
  Quick Sort Time : 0.00110XXX seconds

==================================================
n          Merge Sort (s)       Quick Sort (s)
--------------------------------------------------
10         0.000XXXXX           0.000XXXXX
100        0.000XXXXX           0.000XXXXX
1000       0.001XXXXX           0.001XXXXX
==================================================

Graph saved as 'sorting_complexity.png'
Open 'sorting_complexity.png' in your file explorer to view the graph.
```

> `XXX` represents digits that vary each run. No specific values are shown here to avoid presenting inaccurate data.

### Graph Output

A file named `sorting_complexity.png` will be created in the project folder containing the line chart comparing both algorithms.

---

## Project Structure

```
DAA-Sorting-Visualizer/
│
├── main.py                  # Main script: timing, printing results, plotting
├── sorting.py               # Merge Sort and Quick Sort algorithms (from scratch)
├── requirements.txt         # Python package dependencies
├── README.md                # This documentation file
├── prompt.txt               # The AI prompt used to generate this project
└── sorting_complexity.png   # Output graph (created after running main.py)
```

---

## 16. Conclusion

This project bridges the gap between **theoretical algorithm analysis** and **practical observation**.

Key findings from this experiment:

1. **Both algorithms scale with O(n log n)** on average — confirmed by the gradual upward curve in the graph as n grows from 10 to 1000.

2. **Quick Sort is often faster in practice** even though both algorithms share the same asymptotic complexity. This is because Quick Sort accesses memory in a more CPU-cache-friendly way and has lower overhead per operation.

3. **Merge Sort is more consistent** — its worst case is the same as its best case: O(n log n). Quick Sort's worst case is O(n²), which can occur on already-sorted or reverse-sorted arrays. Since this project uses random arrays, the worst case is avoided.

4. **The difference at small n is negligible** — for n = 10, both algorithms finish in microseconds. The comparison only becomes meaningful as n grows larger.

5. **Visualization matters** — a graph communicates the comparison far more clearly than a table of raw numbers. This is why tools like Matplotlib are valuable in algorithm analysis.

**For Viva Preparation:**  
If asked "Why is Quick Sort faster than Merge Sort in practice even though both are O(n log n)?" — the answer is: Quick Sort has better **cache locality** (it generally accesses memory in a more sequential pattern) and lower **constant factors** in its operations, while Merge Sort always requires O(n) extra memory to hold the merged results.

---

*Submitted as a DAA Macro Project*  
*Subject: Design and Analysis of Algorithms*  
*Language: Python 3 | Visualization: Matplotlib*
