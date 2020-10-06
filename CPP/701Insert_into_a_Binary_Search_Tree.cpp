struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode() : val(0), left(nullptr), right(nullptr) {}
	TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
	TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
    	if (root == nullptr) {
    		return new TreeNode(val);
    	}
    	TreeNode* temp = root;

    	while (root != nullptr) {
    		if (temp->val > val) {
    			if (temp->left == nullptr) {
    				temp->left = new TreeNode(val);
    				break;
    			} 
    			temp = temp->left;
    		} else {
    			if (temp->val < val) {
    				if (temp->right == nullptr) {
    					temp->right = new TreeNode(val);
    					return root;
    				}
    				break;
    			}
    		}
    	}   
    	return root; 
    }
};

void test() {
	TreeNode* root = new TreeNode(2, new TreeNode(1), new TreeNode(4));
	int val = 3;
	Solution* solution = new Solution();
	solution->insertIntoBST(root, val);
}

int main(int argc, char const *argv[])
{
	test();
	return 0;
}

