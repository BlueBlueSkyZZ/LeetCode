package dfs;

public class LC_Offer_54 {

    int leftK, result;

    public int kthLargest(TreeNode root, int k) {
        leftK = k;
        dfs(root);
        return result;
    }

    private void dfs(TreeNode root) {
        if (root == null)
            return;

        dfs(root.right);

        if (leftK <= 0)
            return;
        result = root.val;
        leftK--;

        dfs(root.left);

    }

}
