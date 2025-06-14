class Solution:
    def preorderTraversal(self, root):  # change here if needed
        # Just an example preorder function
        if not root:
            return []
        stack = [root]
        output = []

        while stack:
            node = stack.pop()
            output.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return output
