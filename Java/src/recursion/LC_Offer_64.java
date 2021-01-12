package recursion;

public class LC_Offer_64 {

    public int sumNums(int n) {
        // jump condition
        if (n == 1)
            return 1;

        return n + sumNums(n-1);
    }

}
