package dfs;

public class LC_Offer_28 {

    public boolean isSymmetric(TreeNode root) {
        if (root == null)
            return true;

        return isMirror(root.left, root.right);

    }

    private boolean isMirror(TreeNode treeL, TreeNode treeR) {
        if (treeL == null && treeR == null) {
            return true;
        } else if (treeL != null && treeR != null) {
            if (treeL.val != treeR.val)
                return false;
            return isMirror(treeL.left, treeR.right) && isMirror(treeL.right, treeR.left);
        } else {
            return false;
        }
    }

}
