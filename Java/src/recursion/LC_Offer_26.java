package recursion;


public class LC_Offer_26 {

    public boolean isSubStructure(TreeNode A, TreeNode B) {

        if (A == null)
            return false;

        if (B == null)
            return false;

        return isTheSame(A, B) || isSubStructure(A.left, B) || isSubStructure(A.right, B);

    }

    private boolean isTheSame(TreeNode A, TreeNode B) {
        if (B == null)
            return true;

        if (A == null)
            return false;

        if (A.val != B.val) {
            return false;
        } else {
            return isTheSame(A.left, B.left) && isTheSame(A.right, B.right);
        }

    }

}
