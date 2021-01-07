package array_and_str;

public class LC_Offer_04 {

    public boolean findNumberIn2DArray(int[][] matrix, int target) {

        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int row_left = 0, row_right = matrix[0].length-1, row_mid = (row_left + row_right) / 2;
        int column_left = 0, column_right = matrix.length-1, column_mid;

        while (row_left <= row_right) {
            row_mid = (row_left + row_right) / 2;
            if (matrix[0][row_mid] == target) {
                return true;
            } else if (matrix[0][row_mid] < target) {
                row_left = row_mid + 1;
            } else {
                row_right = row_mid - 1;
            }
        }

        while (column_left <= column_right) {
            column_mid = (column_left + column_right) / 2;
            if (matrix[column_mid][row_mid] == target) {
                return true;
            } else if (matrix[column_mid][row_mid] < target) {
                column_left = column_mid + 1;
            } else {
                column_right = column_mid - 1;
            }
        }

        return false;

    }

    public boolean findNumberIn2DArray2(int[][] matrix, int target) {

        if (matrix.length == 0 || matrix[0].length == 0) {
            return false;
        }

        int row = matrix.length - 1;
        int column = 0;

        while (row >= 0 && column <= matrix[0].length - 1) {
            if (matrix[row][column] == target) {
                return true;
            } else if (matrix[row][column] > target) {
                row -= 1;
            } else {
                column += 1;
            }
        }
        return false;

    }

    public static void main(String[] args) {
        int[][] matrix = {
                {1, 4, 7, 11, 15},
                {2, 5, 8, 12, 19},
                {3, 6, 9, 16, 22},
                {10, 13, 14, 17, 24},
                {18, 21, 23, 26, 30}
        };

        int target = 5;

        LC_Offer_04 sl = new LC_Offer_04();
        System.out.println(sl.findNumberIn2DArray2(matrix, target));
    }

}
