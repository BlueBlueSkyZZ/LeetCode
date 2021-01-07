package array_and_str;

public class LC_Offer_66 {

    public int[] constructArr(int[] a) {

        if (a.length == 0) {
            return new int[]{};
        }

        int[] b = new int[a.length];
        int[] c = new int[a.length];
        int[] d = new int[a.length];

        c[0] = 1;
        d[a.length-1] = 1;
        for (int i = 1; i < a.length; i++) {
            c[i] = c[i-1] * a[i-1];
            d[a.length-1-i] = d[a.length-i] * a[a.length-i];
        }

        for (int i = 0; i < a.length; i++) {
            b[i] = c[i] * d[i];
        }

        return b;
    }

    //time:O(N) space:O(1)
    public int[] constructArr2(int[] a) {

        if (a.length == 0) {
            return new int[0];
        }

        int[] b = new int[a.length];

        b[0] = 1;
        int temp = 1;
        for (int i = 1; i < a.length; i++) {
            b[i] = b[i-1] * a[i-1];
        }

        for (int i = a.length-2; i >= 0; i--) {
            temp *= a[i+1];
            b[i] *= temp;
        }

        return b;
    }

}
