package dp;

import array_and_str.LC_Offer_11;

import java.util.HashMap;
import java.util.Map;

public class LC_Offer_10I {

    public int fib(int n) {
        if (n == 0)
            return 0;
        if (n == 1)
            return 1;

        int fn_1 = 0, fn = 1;
        int temp;
        while (n-2 >= 0) {
            temp = fn;
            fn = (fn_1 + fn) % (int)(1e9+7);
            fn_1 = temp;
            n--;
        }
        return fn;
    }

    // only recursion overtime, we can use hashmap to record the calculated f(n)
    public int fib2(int n) {
        return fib2(n, new HashMap<>());
    }

    private int fib2(int n, Map<Integer, Integer> map) {
        if (n < 2)
            return n;
        if (map.containsKey(n))
            return map.get(n);

        int fn_1 = fib2(n-2, map) % (int)(1e9+7);
        map.put(n-2, fn_1);
        int fn_2 = fib2(n-1, map) % (int)(1e9+7);
        map.put(n-1, fn_2);
        int result = (fn_1 + fn_2) % (int)(1e9+7);
        map.put(n, result);
        return result;

    }

    public static void main(String[] args) {

        LC_Offer_10I lc = new LC_Offer_10I();
        System.out.println(lc.fib2(100));

    }

}
