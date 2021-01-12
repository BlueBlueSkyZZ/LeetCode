package dp;

public class LC_Offer_62 {

    public int lastRemaining(int n, int m) {
        /**
         * f(n,m)=y, f(n-1,m)=x x,y是数组的下标
         * f(n,m)删掉的第一个数下标为(m-1) % n
         * 向右数x+1个数，同时取余n，((m-1)%n+x+1) % n
         * f(n,m)=((m-1)%n+x+1) % n 化简得f(n,m)=(m+x) % n = (m + f(n-1,m) ) % n
         */

        int fn=0;

        for (int i = 2; i <= n; i++) {
            fn = (m + fn) % i;
        }

        return fn;



    }

}
