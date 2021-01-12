package bfs;

import javax.print.DocFlavor;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class LC_Offer_32III {

    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if (root != null)
            queue.add(root);

        while (!queue.isEmpty()) {
            LinkedList<Integer> oneRow = new LinkedList<>();
            for (int i = queue.size(); i > 0; i--) {
                TreeNode node = queue.remove();
                if (result.size() % 2 == 1) {
                    oneRow.addFirst(node.val);
                } else {
                    oneRow.addLast(node.val);
                }
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);
            }
            result.add(new ArrayList<>(oneRow));
        }
        return result;
    }

}
