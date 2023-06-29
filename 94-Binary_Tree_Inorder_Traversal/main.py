
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        subtree = []
        inorder_result = []
        while root or subtree:
            while root:
                subtree.append(root)
                root = root.left
            root = subtree.pop()
            inorder_result.append(root.val)
            root = root.right
        return inorder_result