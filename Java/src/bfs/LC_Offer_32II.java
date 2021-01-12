package bfs;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;
import java.util.stream.Collectors;

public class LC_Offer_32II {

    public List<List<Integer>> levelOrder(TreeNode root) {



        List<List<Integer>> result = new ArrayList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if (root != null)
            queue.add(root);

        while (!queue.isEmpty()) {
            List<Integer> oneRow = new ArrayList<>();
            for (int i = queue.size(); i > 0; i--) {
                TreeNode node = queue.remove();
                oneRow.add(node.val);
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);

            }
            result.add(new ArrayList<>(oneRow));
            oneRow.clear();

        }
        return result;

    }

}
