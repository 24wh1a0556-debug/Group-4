# Project 9 – 0/1 Knapsack using Dynamic Programming

## Description

The 0/1 Knapsack problem is an optimization problem in which each item has a weight and a profit. We have a bag with a fixed maximum capacity and need to select items so that the total weight does not exceed the capacity while getting the maximum possible profit.

In the 0/1 Knapsack problem, each item can either be selected once or not selected. An item cannot be divided.

For this project:

- Number of items: 4
- Knapsack capacity: 10

| Item | Weight | Profit |
|------|--------|--------|
| Item 1 | 2 | 3 |
| Item 2 | 3 | 4 |
| Item 3 | 4 | 5 |
| Item 4 | 5 | 6 |

The optimal selection is Item 1, Item 2 and Item 4.

- Total weight = 2 + 3 + 5 = 10
- Total profit = 3 + 4 + 6 = 13

Therefore, the maximum profit is **13**.

## Algorithm

1. Take the weights, profits, number of items and maximum capacity as input.
2. Create a DP table with `n + 1` rows and `W + 1` columns.
3. Initialize the first row and first column with 0.
4. Consider each item one by one.
5. For each capacity, check whether the current item can fit.
6. If the item does not fit, copy the value from the previous row.
7. If the item fits, calculate:
   - Profit when the item is included.
   - Profit when the item is excluded.
8. Store the larger of these two values in the DP table.
9. After filling the table, `K[n][W]` gives the maximum profit.

## Pseudocode

```text
Algorithm 0/1 Knapsack

Input:
    n = number of items
    W = maximum capacity
    weight[] = weights of items
    profit[] = profits of items

Create DP table K[n+1][W+1]

For i = 0 to n:
    For w = 0 to W:

        If i == 0 OR w == 0:
            K[i][w] = 0

        Else if weight[i-1] <= w:
            K[i][w] = max(
                profit[i-1] + K[i-1][w-weight[i-1]],
                K[i-1][w]
            )

        Else:
            K[i][w] = K[i-1][w]

Return K[n][W]
```

## Algorithm Explanation

Dynamic Programming is used to solve the problem by breaking it into smaller subproblems.

The rows of the DP table represent the items being considered, and the columns represent the available knapsack capacity.

For every item and capacity, the algorithm checks two choices:

- **Include the item:** Add its profit to the best value for the remaining capacity.
- **Exclude the item:** Keep the best value from the previous row.

The larger value is stored in the table. This avoids calculating the same subproblems repeatedly.

## Visualization

The AI-generated visualization shows the complete Dynamic Programming table for 4 items and capacity 10.

The rows represent the items and the columns represent capacities from 0 to 10. The table is filled row by row by comparing the include and exclude choices.

The final cell `K[4][10] = 13` represents the maximum profit that can be obtained without exceeding the capacity of 10.

The visualization makes it easier to understand how the DP table is constructed and how the optimal result is obtained.

## DP Table

```text
        Capacity →
        0  1  2  3  4  5  6  7  8  9  10

0       0  0  0  0  0  0  0  0  0  0   0
Item 1  0  0  3  3  3  3  3  3  3  3   3
Item 2  0  0  3  4  4  7  7  7  7  7   7
Item 3  0  0  3  4  5  7  8  9  9  9  12
Item 4  0  0  3  4  5  7  8  9 10  11  13
```

## Complexity

- Time Complexity: `O(n × W)`
- Space Complexity: `O(n × W)`

where `n` is the number of items and `W` is the maximum capacity.

## Prompt Used

```text
Create a clean academic visualization for the 0/1 Knapsack problem using Dynamic Programming.

Use exactly 4 items:
Item 1: Weight = 2, Profit = 3
Item 2: Weight = 3, Profit = 4
Item 3: Weight = 4, Profit = 5
Item 4: Weight = 5, Profit = 6

Maximum capacity = 10.

Show:
1. A title: "0/1 Knapsack using Dynamic Programming"
2. The four items with their weights and profits.
3. The complete DP table with rows 0, Item 1, Item 2, Item 3, Item 4 and columns for capacities 0 to 10.
4. Clearly show the include and exclude decisions used to fill the table.
5. Highlight the final value K[4][10] = 13.
6. Show the optimal selection: Item 1 + Item 2 + Item 4.
7. Show total weight = 10 and total profit = 13.
8. Use a clean, simple academic style suitable for a DAA college project, PPT and README.
9. Make sure every DP table value is mathematically correct and readable.
```

## Output

**Maximum Profit = 13**

Selected items:

- Item 1
- Item 2
- Item 4

Total weight = **10**

Total profit = **13**

## Learning Outcome

- Understood the 0/1 Knapsack problem.
- Learned how Dynamic Programming is used to solve optimization problems.
- Understood how a DP table is constructed using include and exclude choices.
- Learned how AI tools can be used to create algorithm visualizations.
- Practiced documenting an algorithm and its visualization for a GitHub project.
