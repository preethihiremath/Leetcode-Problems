# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
            
        
        else:
            # Case 1 & 2: Leaf or One Child
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # Case 3: Two Children
            # 1. Find the min value in the right subtree (Successor)
            successor = self.findMin(root.right)
            # 2. Replace current value
            root.val = successor.val
            # 3. Delete the successor node
            root.right = self.deleteNode(root.right, successor.val)
            
        return root

    def findMin(self, node):
        curr = node
        while curr.left:
            curr = curr.left
        return curr