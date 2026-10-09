public class Project9_Knapsack {

    public static int knapsack(int[] weight, int[] profit, int capacity) {

        int n = weight.length;
        int[][] dp = new int[n + 1][capacity + 1];

        for (int i = 1; i <= n; i++) {

            for (int w = 0; w <= capacity; w++) {

                if (weight[i - 1] <= w) {

                    int include = profit[i - 1]
                            + dp[i - 1][w - weight[i - 1]];

                    int exclude = dp[i - 1][w];

                    dp[i][w] = Math.max(include, exclude);

                } else {

                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        System.out.println("DP Table:");

        for (int i = 0; i <= n; i++) {
            for (int w = 0; w <= capacity; w++) {
                System.out.print(dp[i][w] + "\t");
            }
            System.out.println();
        }

        return dp[n][capacity];
    }

    public static void main(String[] args) {

        int[] weight = {2, 3, 4, 5};
        int[] profit = {3, 4, 5, 6};

        int capacity = 10;

        int maximumProfit = knapsack(weight, profit, capacity);

        System.out.println("Maximum Profit = " + maximumProfit);
    }
}