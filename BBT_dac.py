# Definición de la clase TreeNode
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Funcion para ver si el árbol esta balanceado
def is_balanced(root):
    def helper(node):
        if node is None:
            return 0, True

        left_height, left_balanced = helper(node.left)
        right_height, right_balanced = helper(node.right)

        height = max(left_height, right_height) + 1
        balanced = left_balanced and right_balanced and abs(left_height - right_height) <= 1

        return height, balanced

    return helper(root)[1]  # regresa si el árbol esta balanceado o no