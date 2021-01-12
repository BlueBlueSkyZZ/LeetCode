package dp;

public class LC_Offer_10II {

    public int numWays(int n) {
        // dp[n] = dp[n-1] + dp[n-2] dp[2]=2 dp[1]=1 dp[0]=0
        if (n == 0)
            return 1;
        if (n == 1)
            return 1;

        int dp_1=1, dp_2=1;
        int temp;
        while (n - 2 >= 0) {
            temp = dp_2;
            dp_2 = (dp_1 + dp_2) % (int)(1e9+7);
            dp_1 = temp;
            n--;
        }

        return dp_2;
    }

    public static void main(String[] args) {
        int n = 3;
        LC_Offer_10II lc = new LC_Offer_10II();
        System.out.println(lc.numWays(n));
    }


}
