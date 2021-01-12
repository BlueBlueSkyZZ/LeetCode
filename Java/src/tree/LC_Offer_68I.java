package tree;

public class LC_Offer_68I {

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        while ((p.val - root.val) * (q.val - root.val) > 0) {
            if (p.val - root.val < 0 && q.val - root.val < 0) {
                root = root.left;
            } else {
                root = root.right;
            }
        }
        return root;

    }

}
