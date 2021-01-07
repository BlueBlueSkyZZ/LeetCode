package bit;

public class LC_Offer_16 {

    public double myPow(double x, int n) {
        if (x == 0.0f)
            return 0.0d;

        double result = 1.0d;

        long long_n = n; // if n = -2^31

        if (long_n < 0) {
            x = 1/x;
            long_n = -long_n;
        }

        while (long_n > 0) {
            if ((long_n & 1) == 1) {
                result *= x;
            }
                x *= x;
                long_n >>>= 1;
        }
        return result;
    }

    public double myPow2(double x, int n) {
        if (x == 0.0f)
            return 0.0d;

        long long_n = n; // if n = -2^31

        if (long_n < 0) {
            long_n = -long_n;
            return 1 / myPow_recursion(x, long_n);
        }
        return myPow_recursion(x, long_n);

    }

    private double myPow_recursion(double x, long n) {
        if (n == 0)
            return 1;
        if (n == 1)
            return x;

        double result = myPow_recursion(x, n>>1);
        result *= result;

        if ((n & 1) == 1) {
            result *= x;
        }
        return result;
    }


    public static void main(String[] args) {
        double x = 2.0d;
        int n = -10;
        LC_Offer_16 lc = new LC_Offer_16();
        System.out.println(lc.myPow2(x, n));
    }

}
