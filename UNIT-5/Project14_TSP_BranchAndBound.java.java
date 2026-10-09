import java.util.*;

public class Project14_TSP_BranchAndBound {

    static int n = 4;
    static int[][] cost = {
        {0, 10, 15, 20},
        {10, 0, 35, 25},
        {15, 35, 0, 30},
        {20, 25, 30, 0}
    };

    static int[] path = new int[n + 1];
    static boolean[] visited = new boolean[n];
    static int bestCost = Integer.MAX_VALUE;
    static int[] bestPath = new int[n + 1];

    static int calculateBound(int currentCity) {
        int bound = 0;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                int min = Integer.MAX_VALUE;

                for (int j = 0; j < n; j++) {
                    if (i != j && cost[i][j] < min) {
                        min = cost[i][j];
                    }
                }

                bound += min;
            }
        }

        return bound;
    }

    static void tsp(int level, int currentCity, int currentCost) {

        if (level == n) {
            int totalCost = currentCost + cost[currentCity][0];

            System.out.println("Tour: " + getPath() + " -> A"
                    + "   Cost = " + totalCost);

            if (totalCost < bestCost) {
                bestCost = totalCost;

                for (int i = 0; i <= n; i++) {
                    bestPath[i] = path[i];
                }
                bestPath[n] = 0;
            }

            return;
        }

        for (int nextCity = 0; nextCity < n; nextCity++) {

            if (!visited[nextCity]) {

                int newCost = currentCost + cost[currentCity][nextCity];

                visited[nextCity] = true;
                path[level] = nextCity;

                int bound = newCost + calculateBound(nextCity);

                System.out.println(
                    "Checking: " + getPath()
                    + " | Cost = " + newCost
                    + " | Bound = " + bound
                );

                if (bound < bestCost) {
                    tsp(level + 1, nextCity, newCost);
                } else {
                    System.out.println(
                        "Pruned: " + getPath()
                        + " | Bound = " + bound
                    );
                }

                visited[nextCity] = false;
            }
        }
    }

    static String getPath() {
        String result = "";

        for (int i = 0; i < n; i++) {
            result += (char) ('A' + path[i]);

            if (i < n - 1) {
                result += " -> ";
            }
        }

        return result;
    }

    public static void main(String[] args) {

        System.out.println("TSP using Branch and Bound");
        System.out.println("--------------------------");

        System.out.println("Cost Matrix:");

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(cost[i][j] + "\t");
            }
            System.out.println();
        }

        path[0] = 0;
        visited[0] = true;

        System.out.println("\nSearch Process:");
        tsp(1, 0, 0);

        System.out.println("\nOptimal Tour:");

        for (int i = 0; i < n; i++) {
            System.out.print((char) ('A' + bestPath[i]) + " -> ");
        }

        System.out.println("A");
        System.out.println("Minimum Cost = " + bestCost);
    }
}