package array_and_str;

import java.util.ArrayList;

public class LC_Offer_57II {

    public int[][] findContinuousSequence(int target) {
        ArrayList<int[]> list =  new ArrayList<int[]>();
        int small = 1, big = 2;
        int sum;

        while (small + big <= target) {
            sum = small * (big-small+1) + (big-small)*(big-small+1) / 2;
            if (sum == target) {
                int[] subArray = new int[big-small+1];
                for (int i = small; i <= big; i++) {
                    subArray[i-small] = i;
                }
                list.add(subArray);
                big++;
            } else if (sum < target) {
                big++;
            } else {
                small++;
            }
        }
        return list.toArray(new int[list.size()][]);
    }

}
