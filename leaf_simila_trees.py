# Consider all the leaves of a binary tree, from left to right order, the values of those leaves form a leaf value sequence.

# Input: root1 = [3,5,1,6,2,9,8,null,null,7,4], root2 = [3,5,1,6,7,4,2,null,null,null,null,null,null,9,8]
# Output: true


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafNodes(self,root,l):
        if root is None:
            return 
        if root.left is None and root.right is None:
            l.append(root.val)
        if root.left:
            self.getLeafNodes(root.left,l)
        if root.right:
            self.getLeafNodes(root.right,l)
        return l
    

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        l1 =[]
        l2 =[]
        t1_l_n = self.getLeafNodes(root1, l1)
        t2_l_n = self.getLeafNodes(root2, l2)
        if t1_l_n == t2_l_n :
            return True
        else: 
            return False

        