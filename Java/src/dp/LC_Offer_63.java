package dp;

public class LC_Offer_63 {

//    public int maxProfit(int[] prices) {
//        if (prices.length <= 1)
//            return 0;
//        int[][] dp = new int[2][prices.length];
//        dp[0][0] = 0;
//        dp[1][0] = -prices[0];
//        for (int i = 1; i < prices.length; i++) {
//            dp[0][i] = Math.max(dp[0][i-1], dp[1][i-1] + prices[i]);
//            dp[1][i] = Math.max(dp[0][i-1] - prices[i], dp[1][i-1]);
//        }
//
//        return dp[0][prices.length-1];
//    }

    public int maxProfit(int[] prices) {

        int minCost = Integer.MAX_VALUE;
        int maxProfit = 0;

        for (int i = 0; i < prices.length; i++) {
            minCost = Math.min(minCost, prices[i]);
            maxProfit = Math.max(maxProfit, prices[i] - minCost);
        }

        return maxProfit;
    }

}
