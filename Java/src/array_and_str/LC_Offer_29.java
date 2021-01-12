package array_and_str;

import java.lang.reflect.Array;
import java.util.Arrays;

public class LC_Offer_29 {

    public int[] spiralOrder(int[][] matrix) {
        if (matrix.length == 0) {
            return new int[]{};
        }

        int left = 0, top = 0, right = matrix[0].length - 1, bottom = matrix.length - 1;
        int[] result = new int[(right+1)*(bottom+1)];
        int index = 0;
        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                result[index++] = matrix[top][i];
            }
            for (int i = top+1; i <= bottom; i++) {
                result[index++] = matrix[i][right];
            }
            if (left < right && top < bottom) {
                for (int i = right-1; i >= left; i--) {
                    result[index++] = matrix[bottom][i];
                }
                for (int i = bottom-1; i >= top + 1; i--) {
                    result[index++] = matrix[i][left];
                }
            }
            left++;
            right--;
            top++;
            bottom--;
        }

        return result;
    }

    public static void main(String[] args) {

        int[][] matrix  = new int[][]{{1,2,3,4},{5,6,7,8},{9,10,11,12}};
        LC_Offer_29 lc = new LC_Offer_29();
        System.out.println(Arrays.toString(lc.spiralOrder(matrix)));

    }
}
