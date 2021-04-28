from TreeNode import TreeNode


class BinaryTree:
    def __init__(self):
        self.middle = None

    def append_middle(self, data):
        node = TreeNode(data)

        if self.middle is None:
            self.middle = node

    def sort_tree(self, data):
        node = TreeNode(data)

        if self.middle.val > node.val:
            self.middle.left = node

        if self.middle.val < node.val:
            self.middle.right = node


