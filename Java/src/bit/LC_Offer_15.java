package bit;

public class LC_Offer_15 {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;

        while (n != 0) {
            count += (1 & n);
            n >>>= 1;
        }

        return count;

    }

    public int hammingWeight2(int n) {
        int count = 0;

        while (n != 0) {
            count++;
            n = (n & (n-1));
        }
        return count;
    }


    public static void main(String[] args) {
        int n = 00000000000000000000000000001011;
        LC_Offer_15 lc = new LC_Offer_15();
        System.out.println(lc.hammingWeight(n));
    }

}
