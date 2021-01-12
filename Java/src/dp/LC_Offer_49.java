package dp;

public class LC_Offer_49 {

    public int nthUglyNumber(int n) {
        int[] dp = new int[n+1];
        int two = 1, three = 1, five=1;
        dp[1] = 1;
        for (int i = 2; i <= n; i++) {
            dp[i] = Math.min(Math.min(dp[two]*2, dp[three]*3), dp[five]*5);
            if (dp[i] == dp[two] * 2) {
                two++;
            }
            // not else: for example 6 is the common multiple of 2 and 3
            if (dp[i] == dp[three] * 3) {
                three++;
            }
            if (dp[i] == dp[five] * 5) {
                five++;
            }
        }
        return dp[n];
    }

    public static void main(String[] args) {
        int n = 11;
        LC_Offer_49 lc = new LC_Offer_49();
        System.out.println(lc.nthUglyNumber(n));
    }

}
