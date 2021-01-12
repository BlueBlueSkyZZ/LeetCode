package dfs;


import java.util.Stack;

public class LC_Offer_27 {

    public TreeNode mirrorTree(TreeNode root) {
        if (root == null)
            return null;
        TreeNode left = mirrorTree(root.right);
        TreeNode right = mirrorTree(root.left);

        root.left = left;
        root.right = right;

        return root;
    }

    public TreeNode mirrorTree2(TreeNode root) {
        if (root == null)
            return null;

        Stack<TreeNode> stack = new Stack<>();
        stack.push(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pop();
            if (node.left != null)
                stack.push(node.left);
            if (node.right != null)
                stack.push(node.right);

            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;
        }

        return root;

    }

}
