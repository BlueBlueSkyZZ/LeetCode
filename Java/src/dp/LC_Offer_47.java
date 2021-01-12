package dp;

public class LC_Offer_47 {

    public int maxValue(int[][] grid) {
        int m = grid.length, n = grid[0].length;
        int[][] dp = new int[m][n];
        int left, top;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                left = (j-1 >= 0) ? dp[i][j-1] : 0;
                top = (i-1 >= 0) ? dp[i-1][j] : 0;
                dp[i][j] = Math.max(left, top) + grid[i][j];
            }
        }

        return dp[m-1][n-1];
    }

}
